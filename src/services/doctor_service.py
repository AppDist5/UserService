from src.models.doctor import Doctor
from src.config.database import SessionLocal

class DoctorService:
    def __init__(self):
        self.db = SessionLocal()
    
    def create(self, data):
        doctor = Doctor(**data)
        self.db.add(doctor)
        self.db.commit()
        self.db.refresh(doctor)
        return doctor
    
    def find_all(self, especialidad_id=None):
        query = self.db.query(Doctor)
        if especialidad_id:
            query = query.filter(Doctor.especialidadId == especialidad_id)
        return query.all()
    
    def find_by_id(self, doctor_id):
        return self.db.query(Doctor).filter(Doctor.id == doctor_id).first()
    
    def __del__(self):
        self.db.close()