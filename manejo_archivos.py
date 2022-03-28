from io import open

# archivo_texto = open("archivo.txt", "w") #Se reciben dos argumentos. El primero es para el nombre del archivo y el segundo es para el modo. 

# frase = "Estupendo dia para estudiar Python \n el miércoles"

# archivo_texto.write(frase)

# archivo_texto.close() #Cierra el archivo en memoria

# archivo_texto = open("archivo.txt", "r")
archivo_texto = open("archivo.txt", "r+") #lectura y escritura

# texto = archivo_texto.read()

# archivo_texto.close()

# print(texto)

# lineas_texto = archivo_texto.readlines()

# archivo_texto.close()

# print(lineas_texto[0])

# archivo_texto.write("/n Siempre es una buena ocasión para estudiar Python")

# archivo_texto.close()

# print(archivo_texto.read())

# archivo_texto.seek(0) #El método seek sirve para posicionar el puntero
# print(archivo_texto.read())

# archivo_texto.write("Comienzo del texto")

lista_texto = archivo_texto.readlines()

lista_texto[1] = "Esta linea ha sido incluida desde el exterior"

archivo_texto.seek(0)

archivo_texto.writelines(lista_texto)

archivo_texto.close()