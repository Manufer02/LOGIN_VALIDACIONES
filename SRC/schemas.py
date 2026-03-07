from pydantic import BaseModel

class UsuarioCreate(BaseModel):
    correo: str
    password: str
    nombre_usuario: str
    identificacion: str
    celular: str