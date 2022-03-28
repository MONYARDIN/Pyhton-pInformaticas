miLista = ["María", "Pepe", "Martha", "Antonio"]
print(miLista[:]) #Imprime todos los valores de la lista
print(miLista[3])#Imprime un elemento en concreto de la lista
print(miLista[-2])#Con índices negativos se empieza a contar desde el final
print(miLista[0:3])#Imprime los primeros 3 elementos dejando el elemento de índice 3 excluido
print(miLista[:3])#Imprime los mismos elementos de la instrucción anterior
print(miLista[2:])#Imrpime los elemtnos desde el elemento con índice 2 hasta el final de la lista
miLista.append("Sandra")#Agrega un elemento a la lista al final
print(miLista[:])
miLista.insert(2, "Alex")#Inserta un elemento en la lista en el índice en el que le indiquemos
print(miLista[:])
miLista.extend(["Mario", "Fernando"])#Concatena la lista con la que le indiquemos
print(miLista[:])
print(miLista.index("Sandra"))#Nos devuelve el índice del elemento que le indiquemos
print("Pepe" in miLista)#Nos indica si un elemento se encuentra en la lista
miLista.remove("Pepe")#Elimina el elemento de la lista que le indiquemos
print(miLista[:])
miLista.pop()#Elimina el último elemento de una lista
print(miLista[:])
miLista2 = ["Lucia", "Jorge"]
miLista3 = miLista + miLista2
print(miLista3)