#importacion de el objeto
from fastapi import FastAPI

#crear proyecto aplicacion
app = FastAPI()
from controllers.marca_controllers import router
#conectar el grupo de marcas
app.include_router(router=router)