from flask import request, jsonify
from src.services.patient_service import PatientService
import base64

class PatientController:
    def __init__(self):
        self.service = PatientService()
    
    def create(self):
        try:
            data = request.get_json()
            nombre = data.get('nombre')
            apellido = data.get('apellido')
            email = data.get('email')
            telefono = data.get('telefono')
            fechaNacimiento = data.get('fechaNacimiento')
            password = data.get('password')
            
            if not all([nombre, apellido, email, telefono, fechaNacimiento, password]):
                return jsonify({
                    'error': True,
                    'message': 'Todos los campos son obligatorios',
                    'code': 'MISSING_FIELDS'
                }), 400
            
            existing = self.service.find_by_email(email)
            if existing:
                return jsonify({
                    'error': True,
                    'message': 'El email ya está registrado',
                    'code': 'DUPLICATE_EMAIL'
                }), 409
            
            patient = self.service.create(data)
            return jsonify(patient.to_dict()), 201
        except Exception as e:
            return jsonify({
                'error': True,
                'message': 'Error al crear paciente',
                'details': str(e)
            }), 500
    
    def find_all(self):
        try:
            patients = self.service.find_all()
            return jsonify([p.to_dict() for p in patients]), 200
        except Exception as e:
            return jsonify({'error': True, 'message': 'Error al obtener pacientes'}), 500
    
    def find_by_id(self, patient_id):
        try:
            patient = self.service.find_by_id(patient_id)
            if not patient:
                return jsonify({
                    'error': True,
                    'message': 'Paciente no encontrado',
                    'code': 'NOT_FOUND'
                }), 404
            return jsonify(patient.to_dict()), 200
        except Exception as e:
            return jsonify({'error': True, 'message': 'Error al obtener paciente'}), 500
    
    def login(self):
        try:
            data = request.get_json()
            email = data.get('email')
            password = data.get('password')
            
            if not email or not password:
                return jsonify({
                    'error': True,
                    'message': 'Email y contraseña son obligatorios',
                    'code': 'MISSING_CREDENTIALS'
                }), 400
            
            patient = self.service.login(email, password)
            
            if not patient:
                return jsonify({
                    'error': True,
                    'message': 'Credenciales inválidas',
                    'code': 'INVALID_CREDENTIALS'
                }), 401
            
            token = base64.b64encode(f"{patient.id}:{int(__import__('time').time())}".encode()).decode()
            
            return jsonify({
                'success': True,
                'message': 'Login exitoso',
                'token': token,
                'user': {
                    'id': str(patient.id),
                    'nombre': patient.nombre,
                    'apellido': patient.apellido,
                    'email': patient.email
                }
            }), 200
        except Exception as e:
            return jsonify({
                'error': True,
                'message': 'Error en login',
                'details': str(e)
            }), 500