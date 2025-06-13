from sqlalchemy.orm import declarative_base
Base = declarative_base()

from .categoria import categoria
from .modelo import modelo
from .asesoria import asesoria
from .servicio import servicio
from .asesor import asesor
from .historialAsesoria import historialAsesoria
from .tipoAsesoria import tipoAsesoria
from .usuario import usuario
from .blogExperiencia import blogExperiencia
from .galeriaVehiculoModificado import galeriaVehiculoModificado
from .accesorio import accesorio
from .rol import rol
from .vehiculo import vehiculo
from .marca import marca
from .prueba import prueba