from db import Base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Text, Boolean, Date
from sqlalchemy.orm import relationship

class asesor(Base):
    __tablename__ = "asesor"

    idAsesor = Column(Integer, primary_key=True)
    nombreAsesor = Column(String(60))
    apellidoAsesor = Column(String(60))
    correoAsesor = Column(String(60))
    telefonoAsesor = Column(Integer)
    documentoAsesor = Column(Integer)

    # Relación con asesorías
    asesoriasAsesor = relationship("asesoria", back_populates="asesorAsesoria")
