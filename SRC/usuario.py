import re

class Usuario:

    def __init__(self, correo, password, nombre_usuario, identificacion, celular):
        self.correo = correo
        self.password = password
        self.nombre_usuario = nombre_usuario
        self.identificacion = identificacion
        self.celular = celular
# Hola
    # =========================
    # VALIDAR CORREO
    # =========================

    def validar_correo(self):

        if not self.correo:
            return False, "Correo no válido: está vacío"

        patron = r'^[\w\.-]+@[\w\.-]+\.\w+$'

        if not re.match(patron, self.correo):
            return False, "Correo no válido: formato incorrecto"

        return True, "Correo válido"


    # =========================
    # VALIDAR PASSWORD
    # =========================

    def validar_password(self):

        if not self.password:
            return False, "Password no válido: está vacío"

        if len(self.password) < 8:
            return False, "Password no válido: mínimo 8 caracteres"

        if not any(c.isupper() for c in self.password):
            return False, "Password no válido: debe tener una mayúscula"

        if not any(c.isdigit() for c in self.password):
            return False, "Password no válido: debe tener un número"

        return True, "Password válido"


    # =========================
    # VALIDAR NOMBRE
    # =========================

    def validar_nombre_usuario(self):

        if not self.nombre_usuario:
            return False, "Nombre de usuario no válido: está vacío"

        if len(self.nombre_usuario) < 3:
            return False, "Nombre de usuario no válido: mínimo 3 caracteres"

        if not self.nombre_usuario.isalnum():
            return False, "Nombre de usuario no válido: solo letras y números"

        return True, "Nombre de usuario válido"


    # =========================
    # VALIDAR IDENTIFICACION
    # =========================

    def validar_identificacion(self):

        if not self.identificacion.isdigit():
            return False, "Identificación no válida: solo números"

        if len(self.identificacion) > 10:
            return False, "Identificación no válida: máximo 10 dígitos"

        if len(self.identificacion) < 6:
            return False, "Identificación no válida: mínimo 6 dígitos"

        return True, "Identificación válida"


    # =========================
    # VALIDAR CELULAR
    # =========================

    def validar_celular(self):

        if not self.celular.isdigit():
            return False, "Celular no válido: solo números"

        if len(self.celular) != 10:
            return False, "Celular no válido: debe tener exactamente 10 dígitos"

        return True, "Celular válido"
