class Empleado:
    def __init__(self, nombre, departamento, antiguedad):
        self.nombre = nombre
        self.departamento = departamento
        self.antiguedad = antiguedad
    def mostrar(self):
        print(f"Nombre: {self.nombre}, departamento: {self.departamento}, antigüedad en la empresa: {self.antiguedad}")

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
    def estado(self, promedio):
        if promedio >=  7:
            estado = "Satisfactorio"
            return estado
        else:
            estado = "Debe mejorar"
            return estado
    def mostrar(self, promedio):
        print(f"Nota en puntualidad: {self.puntualidad}, nota de trabajo en equipo: {self.equipo}, nota de productividad: {self.productividad}")

class Contacto:
    def __init__(self, email, telefono):
        self.email = email
        self.telefono = telefono
    def mostrar(self):
        print(f"Correo: {self.email}, telefono: {self.telefono}")

empleados = {}
opcion = "0"
while opcion != "3":
    print("\t==CONTROL DE EMPLEADOS==")
    print("1.Registrar empleados")
    print("2.Mostrar información de empleados registrados")
    print("3.Salir")
    opcion = input("\nSeleccione una opción: ")
    try:
        match opcion:
            case "1":
                cantidad = int(input("¿Cuántos empleados desea registrar? (máx 10): "))
                if cantidad < 0 or cantidad > 10:
                    print("Cantidad no fuera de rango")
                    continue
                a = 0
                while a < cantidad:
                    print(f"Datos del empleado {a + 1}:")
                    codigo = input("Codigo del empleado: ")
                    nombre = input("Nombre completo: ")
                    departamento = input("Departamento: ")
                    antiguedad = input("Antigüedad dentro de la empresa: ")
                    nuevo_empleado = Empleado(nombre, departamento, antiguedad)
                    print("\tDatos de evaluación (0-10):")
                    puntualidad = int(input("\tPuntualidad: "))
                    equipo = int(input("\tTrabajo en equipo:"))
                    productividad = int(input("\tProductividad: "))
                    nueva_evaluacion = Evaluacion(puntualidad, equipo, productividad)
                    observacion = input("\tObservaciones: ")
                    promedio = nueva_evaluacion.promedio()
                    estado = nueva_evaluacion.estado(promedio)
                    print("\t\tDatos de contacto: ")
                    telefono = int(input("\t\tTelefono: "))
                    correo = input("\t\tCorreo: ")
                    contacto = Contacto(correo, telefono)
                    empleados[codigo] = {
                        "nombre": nombre,
                        "departamento": departamento,
                        "antiguedad": antiguedad,
                        "evaluacion":{
                            "puntualidad": puntualidad,
                            "equipo": equipo,
                            "productividad": productividad,
                            "observacion": observacion,
                            "promedio": promedio,
                            "estado": estado,
                        },
                        "contacto": {
                            "telefono": telefono,
                            "correo": correo,
                        }
                    }
                    a += 1
            case "2":
                if empleados:
                    print("Empleados registrados:")
                    for codigo, empleado in empleados.items():
                        print(f"Código del empleado {codigo}:")
                        mostrar_empleado = Empleado (empleado["nombre"], empleado["departamento"], empleado["antiguedad"])
                        mostrar_empleado.mostrar()
                        print("Notas de evaluación: ")
                        print(f"\tPuntualidad: {empleado["evaluacion"]["puntualidad"]}, trabajo en equipo: {empleado["evaluacion"]["equipo"]}, productividad: {empleado["evaluacion"]["productividad"]}")
                        print(f"\tObservaiones: {empleado["evaluacion"]['observacion']}")
                        print(f"\tPromedio: {empleado["evaluacion"]['promedio']}, estado: {empleado["evaluacion"]['estado']}")
                        print("Información de contacto: ")
                        print(f"\tTeléfono: {empleado['contacto']['telefono']}")

                else:
                    print("No se ha registrado ningún empleado")
    except Exception as e:
        print("Ha ocurrido un error inseperado, " + str(e))