from sqlalchemy import Column, String, Text
from sqlalchemy.dialects.postgresql import UUID
import uuid
from src.config.database import Base

class Specialty(Base):
    __tablename__ = 'specialties'
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    nombre = Column(String(100), unique=True, nullable=False)
    descripcion = Column(Text, nullable=True)
    
    def to_dict(self):
        return {
            'id': str(self.id),
            'nombre': self.nombre,
            'descripcion': self.descripcion
        }