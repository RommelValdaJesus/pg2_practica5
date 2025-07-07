class Logger:
    _instancia = None

    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)
            cls._instancia.logs = []
        return cls._instancia

    def registrar(self, mensaje):
        self.logs.append(mensaje)

    def obtener_logs(self):
        return self.logs