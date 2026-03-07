from fastapi import FastAPI, Depends
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session
import csv
import os

from SRC.database import engine, Base, SessionLocal
from SRC.models import Usuario as UsuarioModel
from SRC.schemas import UsuarioCreate
from SRC.usuario import Usuario


# Crear tablas en la base de datos
Base.metadata.create_all(bind=engine)


# Crear aplicación FastAPI
app = FastAPI()


# Conexión a la base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Endpoint de prueba
@app.get("/api")
def home():
    return {"mensaje": "API funcionando correctamente"}


# Endpoint de registro
@app.post("/registro")
def registrar(usuario: UsuarioCreate, db: Session = Depends(get_db)):

    usuario_validacion = Usuario(
        usuario.correo,
        usuario.password,
        usuario.nombre_usuario,
        usuario.identificacion,
        usuario.celular
    )

    validaciones = [
        usuario_validacion.validar_correo(),
        usuario_validacion.validar_password(),
        usuario_validacion.validar_nombre_usuario(),
        usuario_validacion.validar_identificacion(),
        usuario_validacion.validar_celular()
    ]

    for resultado, mensaje in validaciones:
        if not resultado:
            return {"error": mensaje}

    nuevo_usuario = UsuarioModel(
        correo=usuario.correo,
        password=usuario.password,
        nombre_usuario=usuario.nombre_usuario,
        identificacion=usuario.identificacion,
        celular=usuario.celular
    )

    db.add(nuevo_usuario)
    db.commit()
    db.refresh(nuevo_usuario)

    return {"mensaje": "Usuario registrado correctamente"}

@app.post("/login")
def login(correo: str, password: str):

    with open("usuarios.csv", newline="") as file:

        reader = csv.DictReader(file)

        for row in reader:

            if row["correo"] == correo and row["password"] == password:

                return {
                    "mensaje": "Login exitoso",
                    "usuario": row["nombre_usuario"]
                }

    return {"error": "Correo o contraseña incorrectos"}


# Mostrar el frontend
app.mount("/", StaticFiles(directory="frontend", html=True), name="frontend")