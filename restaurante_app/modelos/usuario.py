class Usuario:
    ROLES_PERMITIDOS = ("Administrador", "Empleado", "Cliente")

    def __init__(self, identificacion: str, nombre: str, email: str, usuario: str, contrasena: str, rol: str) -> None:
        self.identificacion = identificacion
        self.nombre = nombre
        self.email = email
        self.usuario = usuario
        self.contrasena = contrasena
        self.rol = rol

    @staticmethod
    def validar_texto(valor, campo):
        if not valor or not valor.strip():
            raise ValueError(f"El campo {campo} no puede estar vacio.")

        return valor.strip()

    @property
    def identificacion(self) -> str:
        return self._identificacion

    @identificacion.setter
    def identificacion(self, valor: str) -> None:
        self._identificacion = self.validar_texto(valor, "identificacion")

    @property
    def nombre(self) -> str:
        return self._nombre

    @nombre.setter
    def nombre(self, valor: str) -> None:
        self._nombre = self.validar_texto(valor, "nombre")

    @property
    def email(self) -> str:
        return self._email

    @email.setter
    def email(self, valor: str) -> None:
        self._email = self.validar_texto(valor, "email")

    @property
    def usuario(self) -> str:
        return self._usuario

    @usuario.setter
    def usuario(self, valor: str) -> None:
        self._usuario = self.validar_texto(valor, "usuario")

    @property
    def contrasena(self) -> str:
        return self._contrasena

    @contrasena.setter
    def contrasena(self, valor: str) -> None:
        self._contrasena = self.validar_texto(valor, "contrasena")

    @property
    def rol(self) -> str:
        return self._rol

    @rol.setter
    def rol(self, valor: str) -> None:
        rol_validado = self.validar_texto(valor, "rol")

        if rol_validado not in self.ROLES_PERMITIDOS:
            raise ValueError("El rol seleccionado no es valido.")

        self._rol = rol_validado

    def __str__(self) -> str:
        return f"Usuario: {self.nombre}, Identificacion: {self.identificacion}, Email: {self.email}, Rol: {self.rol}"