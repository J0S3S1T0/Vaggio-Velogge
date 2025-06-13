from db import Base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Text, Boolean, Date
from sqlalchemy.orm import relationship

class marca(Base):
    __tablename__ = "marca"

    idMarca = Column(Integer, primary_key=True)
    nombreMarca = Column(String(50))
    paisOrigenMarca = Column(String(50))

    # Relación con vehículos
    vehiculosMarca = relationship("vehiculo", back_populates="marcaVehiculo")
