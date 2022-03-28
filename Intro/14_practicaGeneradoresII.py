def devuelve_Ciudades(*ciudades):
    for elemento in ciudades:
        # for subElemento in elemento:
        yield from elemento
        
ciudades_devueltas = devuelve_Ciudades("Madrid", "Barcelona", "Bilbao", "Valencia")

print(next(ciudades_devueltas))
print(next(ciudades_devueltas))