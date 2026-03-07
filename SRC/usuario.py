import re

class Usuario:

    def __init__(self, correo, password, nombre_usuario, identificacion, celular):
        self.correo = correo
        self.password = password
        self.nombre_usuario = nombre_usuario
        self.identificacion = identificacion
        self.celular = celular
        
    # =========================
    # VALIDAR CORREO
    # =========================

    def validar_correo(self):
        if not self.correo:
            return False, "❌ El correo no puede estar vacío"
        if not re.match(r"[^@]+@[^@]+\.[^@]+", self.correo):
            return False, "❌ Correo inválido"
        return True, "✅ Correo válido"

    def validar_password(self):
        if not self.password:
            return False, "❌ La contraseña no puede estar vacía"
        if len(self.password) < 8:
            return False, "❌ Mínimo 8 caracteres"
        if not re.search(r"[A-Z]", self.password):
            return False, "❌ Debe tener una mayúscula"
        if not re.search(r"\d", self.password):
            return False, "❌ Debe tener un número"
        return True, "✅ Contraseña válida"

    def validar_nombre_usuario(self):
        if not self.nombre_usuario:
            return False, "❌ Nombre vacío"
        return True, "✅ Nombre válido"

    def validar_identificacion(self):
        if not self.identificacion.isdigit():
            return False, "❌ Solo números"
        if len(self.identificacion) > 10:
            return False, "❌ Máximo 10 dígitos"
        return True, "✅ Identificación válida"

    def validar_celular(self):
        if not self.celular.isdigit():
            return False, "❌ Celular solo números"
        if len(self.celular) > 10:
            return False, "❌ Celular máximo 10 dígitos"
        return True, "✅ Celular válido"
