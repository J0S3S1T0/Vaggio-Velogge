from db import Base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Text, Boolean, Date
from sqlalchemy.orm import relationship

class tipoAsesoria(Base):
    __tablename__ = "tipoAsesoria"

    idTipoAsesoria = Column(Integer, primary_key=True)
    nombreTipoAsesoria = Column(String(50))
    descripcionTipoAsesoria = Column(String(200))

    # Relación con asesorías
    asesoriasTipoAsesoria = relationship("asesoria", back_populates="tipoAsesoriaAsesoria")
