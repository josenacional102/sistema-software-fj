
class ErrorSistema(Exception):
    pass

class DatosInvalidosError(ErrorSistema):
    pass

class ServicioNoDisponibleError(ErrorSistema):
    pass

class ReservaError(ErrorSistema):
    pass
