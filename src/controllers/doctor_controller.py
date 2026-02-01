from flask import request, jsonify
from src.services.doctor_service import DoctorService
from src.services.specialty_service import SpecialtyService

class DoctorController:
    def __init__(self):
        self.service = DoctorService()
        self.specialty_service = SpecialtyService()
    
    def create(self):
        try:
            data = request.get_json()
            nombre = data.get('nombre')
            apellido = data.get('apellido')
            email = data.get('email')
            especialidadId = data.get('especialidadId')
            
            if not all([nombre, apellido, email, especialidadId]):
                return jsonify({
                    'error': True,
                    'message': 'Todos los campos son obligatorios',
                    'code': 'MISSING_FIELDS'
                }), 400
            
            specialty = self.specialty_service.find_by_id(especialidadId)
            if not specialty:
                return jsonify({
                    'error': True,
                    'message': 'Especialidad no encontrada',
                    'code': 'SPECIALTY_NOT_FOUND'
                }), 404
            
            doctor = self.service.create(data)
            return jsonify(doctor.to_dict()), 201
        except Exception as e:
            return jsonify({
                'error': True,
                'message': 'Error al crear médico',
                'details': str(e)
            }), 500
    
    def find_all(self):
        try:
            especialidad = request.args.get('especialidad')
            doctors = self.service.find_all(especialidad)
            return jsonify([d.to_dict() for d in doctors]), 200
        except Exception as e:
            return jsonify({'error': True, 'message': 'Error al obtener médicos'}), 500
    
    def find_by_id(self, doctor_id):
        try:
            doctor = self.service.find_by_id(doctor_id)
            if not doctor:
                return jsonify({
                    'error': True,
                    'message': 'Médico no encontrado',
                    'code': 'NOT_FOUND'
                }), 404
            return jsonify(doctor.to_dict()), 200
        except Exception as e:
            return jsonify({'error': True, 'message': 'Error al obtener médico'}), 500