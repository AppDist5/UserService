from src.models.patient import Patient
from src.config.database import SessionLocal

class PatientService:
    def __init__(self):
        self.db = SessionLocal()
    
    def create(self, data):
        patient = Patient(**data)
        self.db.add(patient)
        self.db.commit()
        self.db.refresh(patient)
        return patient
    
    def find_all(self):
        return self.db.query(Patient).all()
    
    def find_by_id(self, patient_id):
        return self.db.query(Patient).filter(Patient.id == patient_id).first()
    
    def find_by_email(self, email):
        return self.db.query(Patient).filter(Patient.email == email).first()
    
    def login(self, email, password):
        patient = self.find_by_email(email)
        if patient and patient.password == password:
            return patient
        return None
    
    def __del__(self):
        self.db.close()