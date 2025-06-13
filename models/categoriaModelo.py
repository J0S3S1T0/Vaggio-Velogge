from db import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Text, Boolean, Date

class categoriaModelo(Base):
    __tablename__ = "categoriaModelo"

    idCategoriaModelo = Column(Integer, primary_key=True)

    # Llave foránea con id Usurio y id 
    idModelo = Column(Integer, ForeignKey("modelo.idModelo"))
    idAccesorio = Column(Integer, ForeignKey("accesorio.idAccesorio"))