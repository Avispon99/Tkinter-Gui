from tkinter import *

def fun():
	"""impresion en consola"""
	print(var1.get()) # obtiene el texto ingresado por medio de Entry(variable 'textbox') ya almacenado en "var1" a través de 'textvariable'
	"""impresioe en el Label(variable 'lab')"""
	v.set(var1.get()) # Establecer a través de '.set' el valor de 'v', asingando el valor obtenido por var1' obtenido a traves de '.get'

root = Tk()

v = StringVar() # crear variable tipo string.  Nota: Las StringVars deben crarse despues de creal la ventana princípal 
var1= StringVar() # crea variable tipo string

textbox = Entry(root, textvariable = var1) # almacenar el texto ingresado dentro de una variable creada
textbox.pack()

lab= Label(root, textvariable = v)
lab.pack()

butt = Button(root, text='action', command= fun) # boton que activa la funcion(fun) a través de 'command'
butt.pack()


root.mainloop()