from flask import Blueprint, jsonify
from src.controllers.patient_controller import PatientController
from src.controllers.doctor_controller import DoctorController
from src.services.specialty_service import SpecialtyService

user_bp = Blueprint('users', __name__)

patient_controller = PatientController()
doctor_controller = DoctorController()
specialty_service = SpecialtyService()

# Pacientes
@user_bp.route('/patients', methods=['POST'])
def create_patient():
    return patient_controller.create()

@user_bp.route('/patients', methods=['GET'])
def get_patients():
    return patient_controller.find_all()

@user_bp.route('/patients/<patient_id>', methods=['GET'])
def get_patient(patient_id):
    return patient_controller.find_by_id(patient_id)

@user_bp.route('/login', methods=['POST'])
def login():
    return patient_controller.login()

# Médicos
@user_bp.route('/doctors', methods=['POST'])
def create_doctor():
    return doctor_controller.create()

@user_bp.route('/doctors', methods=['GET'])
def get_doctors():
    return doctor_controller.find_all()

@user_bp.route('/doctors/<doctor_id>', methods=['GET'])
def get_doctor(doctor_id):
    return doctor_controller.find_by_id(doctor_id)

# Especialidades
@user_bp.route('/specialties', methods=['GET'])
def get_specialties():
    try:
        specialties = specialty_service.find_all()
        return jsonify([s.to_dict() for s in specialties]), 200
    except Exception as e:
        return jsonify({'error': 'Error al obtener especialidades'}), 500