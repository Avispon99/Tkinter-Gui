from tkinter import *

root = Tk()

"""---------variables---------"""
var1 = StringVar() # variable creada en formato string(debe estar dentro de la raiz o frame creado)
"""-------- Functions--------"""
def fun():
	var1.set('puto vagooooo!') # Asigna el valor a la variable creada
	print('hola mundo')
"""----------------------"""""


root.title('Diccionario Digital')
#root.geometry('550x450')
#root.config(bg='orange')

the_frame = Frame(root) # Frame se empaqueta en la raiz(root), aca tambien se puede meter la config
the_frame.pack(fill='both', expand='True') # tambein serviria 'expand=1'
the_frame.config(width='550', height='470', bg= '#EAEDED' )	# Config se puede usar con cualquiera para no poner todo dentro de la intancia
the_frame.config(relief='sunken', bd=9) #Relief es borde, bd es grosor de borde 

the_label = Label(the_frame, text = 'Esta es una prueba',bg='red', font=(16))
the_label.grid(row = 0, column = 0, padx= 10, pady= 5) # La otra alternativa es el metodo 'place' pero se usan parametros 'x' y 'y'

""" Label sin variable"""
Label(the_frame, text = 'Esta es comentarios',font=(16),bg='red').grid(row = 1, column = 0, padx= 10, pady= 5)


textbox = Entry(the_frame, textvariable= var1) # se asocia la variable
textbox.grid(row = 0, column = 1, padx= 10, pady= 5)

textcoment = Text(the_frame, width= 20, height = 4)
textcoment.grid(row =1, column = 1, padx = 5, pady = 5)
scrollv = Scrollbar(the_frame, command = textcoment.yview)
scrollv.grid(row = 1, column = 2, sticky = 'nsew')
textcoment.config(yscrollcommand = scrollv.set) 

button_1 = Button(root, text= 'accion', command = fun	) # ejectuta la funcion
button_1.pack(pady = 10)  



root.mainloop() 