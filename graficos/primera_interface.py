from tkinter import *

raiz = Tk()

raiz.title("Ventana de Pruebas")

#raiz.resizable(1,1)#width, height. No se va a poder redimensionar la ventana

raiz.iconbitmap("graficos/cara.ico")

#raiz.geometry("650x350")

raiz.config(bg="blue")

miFrame = Frame()

# miFrame.pack(side="left", anchor="n") #Empaquetamos el frame
miFrame.pack(fill="both", expand=True)

miFrame.config(bg="red")

miFrame.config(width="650", height="350")


miFrame.config(bd=10)#borde

miFrame.config(relief="groove")#tipo de borde

miFrame.config(cursor="hand2")


raiz.mainloop() #Bucle infinito. Siempre se coloca al final

#Para abrir la ventana sin una consola detrás debemos de cambiar la extension a .pyw 