from db import Base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Text, Boolean, Date
from sqlalchemy.orm import relationship

class historialAsesoria(Base):
    __tablename__ = "historialAsesoria"

    idHistorialAsesoria = Column(Integer, primary_key=True)
    comentariosHistorialAsesoria = Column(String(500))
    fechaRegistroHistorialAsesoria = Column(Date)

    # Llave foránea con asesorías
    asesoriaIdHistorialAsesoria = Column(Integer, ForeignKey("asesoria.idAsesoria"))
    
    # Relación con asesorías
    asesoriaHistorialAsesoria = relationship("asesoria", back_populates="historialAsesoria")
