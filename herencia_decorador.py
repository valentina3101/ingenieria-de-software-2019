def verificar_ruedas(f):
	def nueva_decorada(self, *args ,**kwargs):
		f(self,*args,*kwargs)
		if self.tipo_vehiculo == 'Auto' and self.posicion %100 == 0:
			print("deberias rotar las ruedas")

		if self.tipo_vehiculo == 'Camion' and self.posicion %20==0:
			print("deberias rotar las ruedas")
	return nueva_decorada

def limite_de_carga(f):
	def nueva_dec(self, *args ,**kwargs):
		f(self,*args,*kwargs)
		if self.kilos > 800:
			print ("estas superando el limite")
	return nueva_dec



class Vehiculo():
	def __init__(self):
		self.posicion = 0

	def tipo_vehiculo(self):
		self.tipo_vehiculo = tipo_vehiculo
		return (self.tipo_vehiculo)
 
class Auto(Vehiculo):
	def __init__(self,**kw):
		super().__init__(**kw)
    
	@verificar_ruedas
	def andar(self):
		self.posicion += 20

	def verificar_ruedas(self):
		print ("rotar ruedas") 

class Camion(Vehiculo):
	def __init__(self,**kw):
		super().__init__(**kw)


	@limite_de_carga
	def andar(self):
		self.posicion += 5
		return self.posicion


	def cargar(self,kilos):
		self.kilos= kilos
		print ((str(self.kilos)) + " " + "kilos cargados")
        

	def verificar_ruedas(self):
		print ("cambiar ruedas")


def manejar_vehiculo(vehiculo):
	for i in range(3):
		vehiculo.andar()
	print  ("quedo en la posicion" +(str(vehiculo.posicion)))


if __name__ == "__main__":
	auto=Auto()
	auto.andar()
	auto.andar()
	auto.andar()
	auto.andar()
	auto.andar()
	auto.verificar_ruedas()
	camion=Camion()
	camion.cargar(980)
	camion.andar()
 
