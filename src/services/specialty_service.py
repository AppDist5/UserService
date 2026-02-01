from src.models.specialty import Specialty
from src.config.database import SessionLocal

class SpecialtyService:
    def create(self, data):
        db = SessionLocal()
        try:
            specialty = Specialty(**data)
            db.add(specialty)
            db.commit()
            db.refresh(specialty)
            return specialty
        except Exception as e:
            db.rollback()
            raise e
        finally:
            db.close()
    
    def find_all(self):
        db = SessionLocal()
        try:
            return db.query(Specialty).all()
        finally:
            db.close()
    
    def find_by_id(self, specialty_id):
        db = SessionLocal()
        try:
            return db.query(Specialty).filter(Specialty.id == specialty_id).first()
        finally:
            db.close()