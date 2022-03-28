from tkinter import *

root = Tk()

miFrame = Frame(root, width=500, height=400)

miFrame.pack()

miImagen = PhotoImage(file="graficos/ironman.png")
# miLabel = Label(miFrame, text="Hola Mundo")
# miLabel.place(x =100, y = 200)

# Label(miFrame, text = "Hola alumnos de Python", fg="red", font=("Comic sans ms", 18)).place(x = 100, y = 200)

Label(miFrame, image=miImagen).place(x=100, y=200)



root.mainloop()