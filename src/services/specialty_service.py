from src.models.specialty import Specialty
from src.config.database import SessionLocal

class SpecialtyService:
    def __init__(self):
        self.db = SessionLocal()
    
    def create(self, data):
        specialty = Specialty(**data)
        self.db.add(specialty)
        self.db.commit()
        self.db.refresh(specialty)
        return specialty
    
    def find_all(self):
        return self.db.query(Specialty).all()
    
    def find_by_id(self, specialty_id):
        return self.db.query(Specialty).filter(Specialty.id == specialty_id).first()
    
    def __del__(self):
        self.db.close()