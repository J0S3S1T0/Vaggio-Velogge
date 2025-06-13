from db import Base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Text, Boolean, Date
from sqlalchemy.orm import relationship

class asesoria(Base):
    __tablename__ = "asesoria"

    idAsesoria = Column(Integer, primary_key=True)
    fechaSolicitudAsesoria = Column(Date)
    estadoAsesoria = Column(String(50))  
    necesidadAsesoria = Column(String(500))

    # Llaves foráneas con id usuario, asesor y tipo de asesoría
    usuarioIdAsesoria = Column(Integer, ForeignKey("usuario.idUsuario"))
    asesorIdAsesoria = Column(Integer, ForeignKey("asesor.idAsesor"))
    tipoAsesoriaIdAsesoria = Column(Integer, ForeignKey("tipoAsesoria.idTipoAsesoria"))

    # Relaciones con Usuario, asesor y tipo de asesoría
    usuarioAsesoria = relationship("usuario", back_populates="asesoriasUsuario")
    asesorAsesoria = relationship("asesor", back_populates="asesoriasAsesor")
    tipoAsesoriaAsesoria = relationship("tipoAsesoria", back_populates="asesoriasTipoAsesoria")

    # Relación con servicio
    serviciosAsesoria = relationship("servicio", back_populates="asesoriaServicio")
