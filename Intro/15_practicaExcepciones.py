def suma(num1, num2):
    return num1+num2

def resta(num1, num2):
    return num1-num2

def multiplicacion(num1, num2):
    return num1*num2

def division(num1, num2):
    try:
        return num1/num2
    except ZeroDivisionError:
        print("No se puede dividir entre 0")
        return "Operación errónea"
while True:
    try:
        op1 = int(input("Ingresa el primer valor: "))
        op2 = int(input("Ingresa el segundo valor: "))
        break
    except ValueError:
        print("Los valores introducidos no son correctos. Inténtalo de nuevo")
    
    
operacion = input("Introduce la operacion a realizar (suma, resta, multiplica, divide): ")

if operacion=="suma":
    print(suma(op1, op2))
elif operacion=="resta":
    print(resta(op1, op2))
elif operacion=="multiplica":
    print(multiplicacion(op1, op2))
elif operacion=="divide":
    print(division(op1, op2))
else:
    print("operacion no contemplada")