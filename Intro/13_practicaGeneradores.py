# def generaPares (limite):
#     num = 1
#     miLista=[]
    
#     while num<limite:
#         miLista.append(num*2)
#         num=num+1
#     return miLista

# print(generaPares(10))


def generaPares(limite):
    num=1
    while num<limite:
        yield num*2
        num=num+1
devuelvePares=generaPares(10)  
print(next(devuelvePares))
print("Codigo")
print(next(devuelvePares))
print("Codigo")
print(next(devuelvePares))
