from db import Base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Text, Boolean, Date
from sqlalchemy.orm import relationship

class galeriaVehiculoModificado(Base):
    __tablename__ = "galeriaVehiculoModificado"

    idGaleriaVehiculoModificado = Column(Integer, primary_key=True)
    nombreVehiculoGaleriaVehiculoModificado = Column(String(100))
    descripcionGaleriaVehiculoModificado = Column(String(100))

    # Llaves foráneas con usuario y vehículo
    usuarioIdGaleriaVehiculoModificado = Column(Integer, ForeignKey("usuario.idUsuario"))
    vehiculoIdGaleriaVehiculoModificado = Column(Integer, ForeignKey("vehiculo.idVehiculo"))

    # Relaciones con usuario y vehículo
    usuarioGaleriaVehiculoModificado = relationship("usuario", back_populates="galeriaUsuario")
    vehiculoGaleriaVehiculoModificado = relationship("vehiculo", back_populates="galeriaVehiculo")
