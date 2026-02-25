from SRC.usuario import Usuario

print("=== VALIDACIÓN DETALLADA DE USUARIO ===\n")

usuario = Usuario(
    correo="correo@gmail.com",
    password="Password1",
    nombre_usuario="fernando",
    identificacion="1234567890",
    celular="3001234567"
)

validaciones = [
    usuario.validar_correo(),
    usuario.validar_password(),
    usuario.validar_nombre_usuario(),
    usuario.validar_identificacion(),
    usuario.validar_celular()
]

for resultado, mensaje in validaciones:
    print(mensaje)