from db import Base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Text, Boolean, Date
from sqlalchemy.orm import relationship

class blogExperiencia(Base):
    __tablename__ = "blogExperiencia"

    idBlogExperiencia = Column(Integer, primary_key=True)
    fechaPublicidadBlogExperiencia = Column(String(500))

    # Llave foránea con usuario
    usuarioIdBlogExperiencia = Column(Integer, ForeignKey("usuario.idUsuario"))

    # Relación con usuario
    usuarioBlogExperiencia = relationship("usuario", back_populates="blogsUsuario")
