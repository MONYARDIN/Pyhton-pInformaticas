miDiccionario = {"Alemania":"Berlín", "Francia":"París", "Reino Unido":"Londres", "España":"Madrid"}

print(miDiccionario["Francia"])
print(miDiccionario["España"])
print(miDiccionario)
miDiccionario["Italia"] = "Lisboa" #Agregamos un nuevo elemento al diccionario
print(miDiccionario)
miDiccionario["Italia"] = "Roma" #Modificamos el valor de la clave Italia
print(miDiccionario)
del miDiccionario["Reino Unido"] #Eliminamos un elemento del diccionario
print(miDiccionario)
miDiccionario2 = {"Alemania":"Berlín", 23:"Jordan", "Mosqueteros":3}
print(miDiccionario2)
miTupla = ["España","Francia","Reino Unido","Alemania"]
miDiccionario3 = {miTupla[0]:"Madrid", miTupla[1]:"Paris", miTupla[2]:"Londres", miTupla[3]:"Berlín"}
print(miDiccionario3)
miDiccionario4 = {23:"Jordan", "Nombre":"Michael", "Equipo":"Chicago", "Anillos":[1991, 1992, 1993, 1996, 1997, 1998]}
print(miDiccionario4)
print(miDiccionario4["Anillos"])
miDiccionario5 = {23:"Jordan", "Nombre":"Michael", "Equipo":"Chicago", "Anillos":{"temporadas":[1991, 1992, 1993, 1996, 1997, 1998]}}
print(miDiccionario5["Anillos"])
print(miDiccionario5.keys())
print(miDiccionario5.values())
print(len(miDiccionario5))