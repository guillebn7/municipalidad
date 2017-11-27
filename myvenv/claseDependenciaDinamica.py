class Dependencia():
	def __init__(self, nombre, domicilio, telefono): # constructor
		self.nombre = nombre
		self.domicilio = domicilio
		self.telefono = telefono

	def __str__(self):
		return(self.getNom + self.getDom + self.getTel) 

	def setNom(self, nom):
		self.nombre = nom

	def setDom(self, dom):
		self.domicilio = dom

	def setTel(self, tel):
		self.telefono = tel

	def getNom(self):
		return(self.nombre)

	def getDom(self):
		return(self.domicilio)

	def getTel(self):
		return(self.telefono)

   
lista = []
seguirCargando = "si"

while (seguirCargando == "si"):

    print("Ingrese Nombre de Dependencia")
    nombre = input()

    print("Ingrese Domicilio de " + nombre)
    domicilio = input()

    print("Ingrese Telefono de " + nombre)
    telefono = input()

    dep = Dependencia(nombre, domicilio, telefono)
    lista.append(dep)         

    print("Dependencia " + dep.getNom())
    print("Direccion: " + dep.getDom())
    print("Contacto: " + dep.getTel())

    print("Cargar otra Dependencia? si/no: ")
    seguirCargando = input()

print (lista[0:].__str__())