from db import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Text, Boolean, Date

class accesorio(Base):
    __tablename__ = "accesorio"

    idAccesorio = Column(Integer, primary_key=True)
    nombreAccesorio = Column(String(100))
    descripcionAccesorio = Column(String(50))
    precioAccesorio = Column(Integer)

    # Llave foránea con el idVehiculos
    vehiculoIdAccesorio = Column(Integer, ForeignKey("vehiculo.idVehiculo"))

    # Relación con vehículos
    vehiculoAccesorio = relationship("vehiculo", back_populates="accesoriosVehiculo")
