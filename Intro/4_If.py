print("Programa de evaluación de calificaciones")
nota_alumno = input("Introduce la calificación: ")

def evaluacion(nota):
    valoracion = "aprobado"
    if nota < 5:
        valoracion = "reprobado"
    return valoracion

print(evaluacion(int(nota_alumno)))


