from db import Base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Text, Boolean, Date
from sqlalchemy.orm import relationship

class rol(Base):
    __tablename__ = "rol"

    idRol = Column(Integer, primary_key=True)
    nombreRol = Column(String(60))
    estadoRol = Column(String(60))
    descripcionRol = Column(String(60))

    # Relación con usuarios
    usuariosRol = relationship("usuario", back_populates="rolUsuario")
