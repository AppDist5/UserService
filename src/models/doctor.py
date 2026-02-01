from sqlalchemy import Column, String, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from datetime import datetime
import uuid
from src.config.database import Base

class Doctor(Base):
    __tablename__ = 'doctors'
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    nombre = Column(String(100), nullable=False)
    apellido = Column(String(100), nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    especialidadId = Column(UUID(as_uuid=True), ForeignKey('specialties.id'), nullable=False)
    createdAt = Column(DateTime, default=datetime.utcnow)
    
    especialidad = relationship('Specialty', backref='doctors')
    
    def to_dict(self):
        return {
            'id': str(self.id),
            'nombre': self.nombre,
            'apellido': self.apellido,
            'email': self.email,
            'especialidadId': str(self.especialidadId),
            'especialidad': self.especialidad.to_dict() if self.especialidad else None,
            'createdAt': self.createdAt.isoformat() if self.createdAt else None
        }