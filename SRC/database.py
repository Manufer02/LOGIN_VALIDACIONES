@app.post("/registro")
def registrar(usuario: UsuarioCreate):

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

    archivo = "usuarios.csv"

    archivo_existe = os.path.isfile(archivo)

    with open(archivo, mode="a", newline="") as file:
        writer = csv.writer(file)

        if not archivo_existe:
            writer.writerow(["correo","password","nombre_usuario","identificacion","celular"])

        writer.writerow([
            usuario.correo,
            usuario.password,
            usuario.nombre_usuario,
            usuario.identificacion,
            usuario.celular
        ])

    return {"mensaje": "Usuario registrado correctamente"}