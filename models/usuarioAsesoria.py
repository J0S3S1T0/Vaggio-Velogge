from db import Base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Text, Boolean, Date
from sqlalchemy.orm import relationship

class usuarioAsesoria(Base):
    __tablename__ = "usuarioAsesoria"
    
    idUsuarioAsesoria = Column(Integer, primary_key=True)
    
    # Llave foránea con id Usurio y id 
    idUsuario = Column(Integer, ForeignKey("usuario.idUsuario"))
    idAsesoria = Column(Integer, ForeignKey("asesoria.idAsesoria"))