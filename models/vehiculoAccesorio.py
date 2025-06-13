from db import Base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Text, Boolean, Date
from sqlalchemy.orm import relationship

class vehiculoAccesorio(Base):
    __tablename__ = "vehiculoAccesorio"
    
    idVehiculoAccesorio = Column(Integer, primary_key=True)
    
    # Llave foránea con id Usurio y id 
    idAccesorio = Column(Integer, ForeignKey("accesorio.idAccesorio"))
    idVehiculo = Column(Integer, ForeignKey("vehiculo.idVehiculo"))