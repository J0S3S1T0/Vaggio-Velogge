from db import Base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Text, Boolean, Date
from sqlalchemy.orm import relationship

class modelo(Base):
    __tablename__ = "modelo"

    idModelo = Column(Integer, primary_key=True)
    referenciaModelo = Column(String(60))
    marcaModelo = Column(String(60))
    fechaLanzamientoModelo = Column(Date)

    # Llave foránea con la tabla categoria y el atributo id
    categoriaIdModelo = Column(Integer, ForeignKey("categoria.idCategoria"))

    # Relación con categoria
    categoriaModelo = relationship("categoria", back_populates="modelosCategoria")
