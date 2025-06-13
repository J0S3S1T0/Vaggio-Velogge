from db import Base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Text, Boolean, Date
from sqlalchemy.orm import relationship

class servicio(Base):
    __tablename__ = "servicio"

    idServicio = Column(Integer, primary_key=True)
    descripcionServicio = Column(String(60))
    estadoServicio = Column(String(60))

    # Llave foránea con id asesorías
    asesoriaIdServicio = Column(Integer, ForeignKey("asesoria.idAsesoria"))

    # Relación con asesoría
    asesoriaServicio = relationship("asesoria", back_populates="serviciosAsesoria")
