# for i in ["Pildoras", "Informáticas", 3]:
#     print("Hola", end=" ")

# contador = 0 

# email = False
# miEmail = input("Introduce tu dirección de email: ")
# for i in miEmail:
#     if(i == "@" or i == "."):
#         contador = contador + 1
        
# if contador == 2:
#     print("Email es correcto")
# else:
#     print("Email es incorrecto")

# for i in range(5, 50, 3):
#     print(f"valor de la variable {i}")
    
valido = False

email = input("Introduce tu email: ")

for i in range(len(email)):
    if email[i]=="@":
        valido = True
        
if valido:
    print("email correcto")
else:
    print("Email incorrecto")