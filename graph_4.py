import tkinter 

def fun_2(): # After repeta los 5 segundos para ejecutar la fun_2, lo que significa que after solo influye en su funcion asiganada
	var.set('CAMBIO')
	print('XXXXXXXXX')

def fun():

	root.withdraw() # oculta ventana 

	root_2 = tkinter.Toplevel() #crea ventana secundaria

	aviso = tkinter.Label(root_2, textvariable = var)
	aviso.pack()
    
	aviso.after(5000, fun_2) # After tambien se puede usar en otro tipo de objetos como Label y no solo en la raiz('Tk')

	root.after(10000, root.destroy) # After No inpide que 'yyyyyy' se imprima inmediato, lo que recuerda a un hilo..
	print('yyyyyyyyyy')


root = tkinter.Tk()

var = tkinter.StringVar()
var.set('hola desde la v.secundaria') # Debia estableserse el set  para que var no no fuera tipo 'str' sino 


boton = tkinter.Button(root, text='action', command=fun).pack()


root.mainloop()

"""NOTA: Metodos como por ejemplo Tk() o Button() o Label() estan al mismo nivel de instancia de clase
   mientras que por ejemplo after() o withdraw() o pack() son methodos de uso en dichas instancias"""
