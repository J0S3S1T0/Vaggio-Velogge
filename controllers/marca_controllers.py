from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from models.marca import marca
from dtos.marca_dto import MarcaDTO
from db.session import SessionLocal



#objeto qe contiene un rutaro 
#para create

def get_session():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


router = APIRouter(prefix="/marca")
@router.get('/')
def listar():
    return "lista de marcas"

#ruta parametrizada
@router.get('/{id}')
def listar_por_id(id: int):
    return "listar marcas id es" + str(id)

#ruta post
@router.post("/")
def crear_marca(nueva_marca: MarcaDTO,
                db: Session = Depends(get_session)):
    #agregar crear categoria
    nc = marca(
        nombreMarca=nueva_marca.nombreMarca,
        paisOrigenMarca=nueva_marca.paisOrigenMarca
    )
            
    #insertar nueva categoria
    db.add(nc)
    #confirmar transaccion
    db.commit()
    #nueva categoria en el proyecto
    db.refresh(nc)
    return nc


#ruta put update
@router.put("/{id}")
def actualizar_marca(id: int):
    return "actualizar marca" + str(id)

#ruta delete
@router.delete("/{id}")
def eliminar_marca(id: int):
    return "eliminar marca" + str(id)