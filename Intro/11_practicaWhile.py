# i = 1

# while i<10:
#     print("Ejecución " + str(i))
#     i = i+1
# print("Terminó la ejecución")

# edad = int(input("Introduce tu edad: "))

# while edad < 0 or edad>100:
#     print("Introduciste una edad incorrecta. Vuelve a intentarlo")
#     edad = int(input("Introduce tu edad por favor: "))
# print("Gracias por colaborar")
# print("Edad del aspirante " + str(edad))

import math


print("Programa de calculo de raiz cuadrada")
numero = int(input("Introduce un numero por favor: "))

intentos = 0

while numero<0:
    print("No se puede hallar la raiz de un número negativo")
    
    if intentos==2:
        print("Has consumido demasiados intentos. El programa ha finalizado")
        break;
    numero=int(input("Introduce un numero por favor: "))
    if numero<0:
        intentos=intentos+1
        
if intentos<2:
    solucion=math.sqrt(numero)
    print("La raiz cuadrada de " + str(numero) + " es " + str(solucion))