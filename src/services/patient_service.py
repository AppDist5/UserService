from src.models.patient import Patient
from src.config.database import SessionLocal

class PatientService:
    def create(self, data):
        db = SessionLocal()
        try:
            patient = Patient(**data)
            db.add(patient)
            db.commit()
            db.refresh(patient)
            return patient
        except Exception as e:
            db.rollback()
            raise e
        finally:
            db.close()
    
    def find_all(self):
        db = SessionLocal()
        try:
            return db.query(Patient).all()
        finally:
            db.close()
    
    def find_by_id(self, patient_id):
        db = SessionLocal()
        try:
            return db.query(Patient).filter(Patient.id == patient_id).first()
        finally:
            db.close()
    
    def find_by_email(self, email):
        db = SessionLocal()
        try:
            return db.query(Patient).filter(Patient.email == email).first()
        finally:
            db.close()
    
    def login(self, email, password):
        db = SessionLocal()
        try:
            patient = db.query(Patient).filter(Patient.email == email).first()
            if patient and patient.password == password:
                return patient
            return None
        finally:
            db.close()