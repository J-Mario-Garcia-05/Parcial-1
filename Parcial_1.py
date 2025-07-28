class Empleado:
    def __init__(self, nombre, departamento, antiguedad):
        self.nombre = nombre
        self.departamento = departamento
        self.antiguedad = antiguedad

class Evaluacion:
    def __init__(self, puntualidad, equipo, productividad):
        self.__puntualidad = puntualidad
        self.__equipo = equipo
        self.__productividad = productividad
    @property
    def puntualidad(self):
        return self.__puntualidad
    @puntualidad.setter
    def puntualidad(self, puntualidad):
        if 0 <= puntualidad <= 10:
            self.__puntualidad = puntualidad
        else:
            print("Nota en puntualidad fuera de rango")
    @property
    def equipo(self):
        return self.__equipo
    @equipo.setter
    def equipo(self, equipo):
        if 0 <= equipo <= 10:
            self.__equipo = equipo
        else:
            print("Nota en equipo fuera de rango")
    @property
    def productividad(self):
        return self.__productividad
    @productividad.setter
    def productividad(self, productividad):
        if 0 <= productividad <= 10:
            self.__productividad = productividad
        else:
            print("Nota en productividad fuera de rango")
    def promedio(self):
        return (self.productividad + self.equipo + self.puntualidad) / 3

class Contacto:
    def __init__(self, email, telefono):
        self.email = email
        self.telefono = telefono