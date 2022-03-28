miTupla = ("Juan", 13, 1, 1995, 13)
miLista2 = ["Alexis", 13, 2, 1999]
miTupla2 = tuple(miLista2) #Convertimos una tupla en una lista
miLista = list(miTupla) #Convertimos nuestra tupla en una lista
print(miTupla[2]) #Accedemos a un elemento de la tupla y lo imprimimos
print(miLista)
print(miTupla)
print(miLista2)
print(miTupla2)
print("Juan" in miTupla) #Preguntamos si un elemento se encuentra dentro de un tupla
print(miTupla.count(13)) #Con el método count nos indica cuantas veces aparece el elemento que le indiquemos
print(len(miTupla2)) #El método len sirve para saber cuantos elementos hay en una tupla
miTupla3 = ("Alberto",) #Tupla unitaria
print(len(miTupla3))
miTupla4 = "Jose", 13, 1, 1997 #Esta es otra forma de declarar una tupla. Conocido como empaquetado de tupla
print(miTupla4)
nombre, dia, mes, agno = miTupla4 #Desempaquetado de tupla
print(nombre)
print(dia)
print(agno)
print(mes)