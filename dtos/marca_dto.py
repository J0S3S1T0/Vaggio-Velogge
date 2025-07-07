from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class MarcaDTO(BaseModel):
    nombreMarca: str
    paisOrigenMarca: str