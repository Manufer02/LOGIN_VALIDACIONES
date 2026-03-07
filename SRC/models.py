from sqlalchemy import Column, Integer, String
from SRC.database import Base

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    correo = Column(String, unique=True, index=True)
    password = Column(String)
    nombre_usuario = Column(String)
    identificacion = Column(String)
    celular = Column(String)