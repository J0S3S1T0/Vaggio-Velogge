from db import Base
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Text, Boolean, Date
from sqlalchemy.orm import relationship

class categoria(Base):
    __tablename__ = "categoria"

    idCategoria = Column(Integer, primary_key=True)
    estadoCategoria = Column(String(45))
    nombreCategoria = Column(String(60))

    # Relación con modelos
    modelosCategoria = relationship("modelo", back_populates="categoriaModelo")