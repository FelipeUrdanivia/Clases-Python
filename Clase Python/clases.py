class Persona():
    def __init__(self,nombre):
        self.nombre = nombre
class Empresa():
    def __init__(self,nombre):
        self.nombre = nombre
        self.empleados = []
    def agregar_empleado(self,empleado):
        self.empleados.append(empleado)
class Empleado(Persona):
    def __init__(self, nombre):
        super().__init__(nombre)

juan = Empleado("Juan")
santander = Empresa("Santander")
santander.agregar_empleado(juan)
print(santander.empleados[0].nombre)