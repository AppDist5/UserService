from sqlalchemy import Column, String, Date, DateTime
from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime
import uuid
from src.config.database import Base

class Patient(Base):
    __tablename__ = 'patients'
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    nombre = Column(String(100), nullable=False)
    apellido = Column(String(100), nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    telefono = Column(String(20), nullable=False)
    fechaNacimiento = Column(Date, nullable=False)
    password = Column(String(255), nullable=False)
    createdAt = Column(DateTime, default=datetime.utcnow)
    
    def to_dict(self):
        return {
            'id': str(self.id),
            'nombre': self.nombre,
            'apellido': self.apellido,
            'email': self.email,
            'telefono': self.telefono,
            'fechaNacimiento': self.fechaNacimiento.isoformat() if self.fechaNacimiento else None,
            'createdAt': self.createdAt.isoformat() if self.createdAt else None
        }