from src.models.doctor import Doctor
from src.config.database import SessionLocal

class DoctorService:
    def create(self, data):
        db = SessionLocal()
        try:
            doctor = Doctor(**data)
            db.add(doctor)
            db.commit()
            db.refresh(doctor)
            return doctor
        except Exception as e:
            db.rollback()
            raise e
        finally:
            db.close()
    
    def find_all(self, especialidad_id=None):
        db = SessionLocal()
        try:
            query = db.query(Doctor)
            if especialidad_id:
                query = query.filter(Doctor.especialidadId == especialidad_id)
            return query.all()
        finally:
            db.close()
    
    def find_by_id(self, doctor_id):
        db = SessionLocal()
        try:
            return db.query(Doctor).filter(Doctor.id == doctor_id).first()
        finally:
            db.close()
