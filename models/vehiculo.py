from db import Base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Text, Boolean, Date
from sqlalchemy.orm import relationship

class vehiculo(Base):
    __tablename__ = "vehiculo"

    idVehiculo = Column(Integer, primary_key=True)
    marcaVehiculo = Column(String(50))
    modeloVehiculo = Column(String(50))
    añoVehiculo = Column(Integer)
    tipoVehiculo = Column(String(50))
    descripcionTecnicaVehiculo = Column(String(50))

    # Llaves foráneas con modelos y marcas
    modeloIdVehiculo = Column(Integer, ForeignKey("modelo.idModelo"))
    marcaIdVehiculo = Column(Integer, ForeignKey("marca.idMarca"))

    # Relaciones con modelo, marca y accesorios
    modeloVehiculo = relationship("modelo", back_populates="vehiculosModelo")
    marcaVehiculo = relationship("marca", back_populates="vehiculosMarca")
    accesoriosVehiculo = relationship("accesorio", back_populates="vehiculoAccesorio")
