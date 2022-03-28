
class Coche():
    
    def __init__(self): #Constructor de la clase
        self.__largoChasis = 250
        self.__anchoChasis = 120
        self.__ruedas = 4 #Al colocar __antes de la propiedad la encapsulamos
        self.__enmarcha = False
    
    def arrancar(self, arrancamos):
        self.__enmarcha = arrancamos
        
        if(self.__enmarcha):
            chequeo=self.__chequeoInterno()
            
        if(self.__enmarcha and chequeo):
            return "El coche está en marcha"
        elif(self.__enmarcha and chequeo == False):
            return "Algo ha ido mal en el chequeo"
        else:
            return "El coche está parado"
        
    def estado(self):
        print("El coche tiene ", self.__ruedas, "ruedas. Un ancho de ", self.__anchoChasis, " y un largo de ", self.__largoChasis)
        
    def __chequeoInterno(self):
        print("Realizando chequeo interno")
        self.gasolina = "ok"
        self.aceite = "mal"
        self.puertas = "cerradas"
        
        if(self.gasolina=="ok" and self.aceite=="ok" and self.puertas=="cerradas"):
            return True
        else:
            return False        
    

miCoche = Coche() #Instanciar una clase en python

print(miCoche.arrancar(True))
miCoche.estado()

print("==============A continuación creamos el segundo objeto=================")

miCoche2=Coche()
print(miCoche2.arrancar(False))
miCoche2.estado()