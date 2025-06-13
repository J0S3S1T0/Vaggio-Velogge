from db import Base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Text, Boolean, Date
from sqlalchemy.orm import relationship

class usuario(Base):
    __tablename__ = "usuario"

    idUsuario = Column(Integer, primary_key=True)
    nombreUsuario = Column(String(60))
    contraseñaUsuario = Column(String(60))
    telefonoUsuario = Column(Integer)
    documentoUsuario = Column(Integer)
    edadUsuario = Column(Integer)
    correoUsuario = Column(String(60))

    # Llave foránea con id rol
    rolIdUsuario = Column(Integer, ForeignKey("rol.idRol"))

    # Relaciones con asesorías, blogs y roles
    asesoriasUsuario = relationship("asesoria", back_populates="usuarioAsesoria")
    blogsUsuario = relationship("blogExperiencia", back_populates="usuarioBlog")
    rolUsuario = relationship("rol", back_populates="usuariosRol")
