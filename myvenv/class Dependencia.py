class Dependencia():
	def __init__(self, nombre, domicilio, telefono): # constructor
		self.nombre = nombre
		self.domicilio = domicilio
		self.telefono = telefono

	def setNom(self, nom):
		self.nombre = nom

	def setDom(self, dom):
		self.domicilio = dom

	def setTel(self, tel):
		self.telefono = tel

	def getNom(self):
		print(nombre)

	def getDom(self):
		print(domicilio)

	def getTel(self):
		print(telefono)

	def mostrarDep(self):
        print("1")

dep1 = Dependencia("Cultura", "Constitución 965", "4671432")
dep1.mostrarDep()

raw_imput()
