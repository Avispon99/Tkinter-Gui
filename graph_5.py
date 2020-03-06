import tkinter


# EJEMPLO 1 (HEREDAR DE RAIZ)
"""
class Test(tkinter.Tk):
	def __init__(self):
		super().__init__() # Si se hereda de Tk el 'super().' solo se requiere si se usa el metodo '__init__' de lo contrario genera error de recursión

ins=Test() # al heredar de 'tkinter.Tk' cuenta como crear la intanciacion de un 'Tk' normal
tkinter.Button(ins,text='HOLA').pack()
ins.mainloop()
"""


# EJEMPLO 2 (HEREDAR DE BOTON)
"""
class Test(tkinter.Button):
	def __init__(self,ven): # ven se pasa como parametro para que interactue con la herencia button siendo
		super().__init__(ven, text='hola') # el 'super().' parece ser indispensable en una herencia de Tkinter, epecialmente si hereda de una clase que debe se empaquetada ej: 'Button'

ven=tkinter.Tk()
ins=Test(ven).pack() # al heredar de 'tkinter.Button' cuenta como crear la inStanciacion de un 'Button' normal
ven.mainloop()
"""


# EJEMPLO 3 (HEREDAR SIN SUPER para Tk)
"""
class Test(tkinter.Tk):
	
	def imprimir(self):
		print('hello world')

ins = Test()
but = tkinter.Button(ins, text='BOTON')
but.pack() 
ins.imprimir()
ins.mainloop()
"""


# EJEMPLO 4 (HEREDAR CON SUPER Y CON SECUENCIA DE LLAMADAS EN __INIT__, y con aclaracion de funcinamiento de parametros en python)
"""
class Test(tkinter.Button):
	def __init__(self, ventana, equis):
		self.equis = equis # solo se usa esta forma de asignacion si se va a llamar la variable desde otro metodo con la variable del argumento de la funcion en lugar de hacerlo con el parametro de la instancia
		self.y = 'yyyyy'
		self.cuadrotext() # Elemento a empaquetar llamado desde dentro de la clase
		super().__init__(ven, text=' el botton') # en las funciones y metodos no influye si se llama el parametro desde parametro de la instancia('ven') o desde argumento de la funcion('ventana')			

	def imprimir(self):
		print('\nola k ase :v ' + x , self.y) # aca se puede llamar a x desde otro metodo directamente desde el parametro de la instancia sin usar 'equis'
		print('\nno hago un culo ' + self.equis) # aca se llama equis con el metodo conocido de asignar una variable tipo 'self' al argumento('equis') de la funcion	

	def cuadrotext(self):
		tkinter.Entry(ven).pack()
		self.imprimir()

	def textlabel(self):
		tkinter.Label(text='Este es un Label..').pack()

ven = tkinter.Tk()
x = 'XXXX'
but = Test(ven,x)
but.pack()
but.textlabel() #  elemento a empaquetar llamado desde fuera de la clase
ven.mainloop()
"""


# EJEMPLO 5 (CLASE HEREDADA EMPAQUETADA EN OTRA CLASE HEREDADA)
"""
class Test(tkinter.Tk):
	pass

ins = Test()

class Bot(tkinter.Button):
	def __init__(self, ins):
		super().__init__(ins, text='Doble class')

but = Bot(ins).pack()

ins.mainloop()
"""

# EJEMPLO 6 (Tkinter pero usando clase normal SIN Herencia)
"""
class Test():
	def Lab(self): # Frame('fram') pudo ser utilizado para empaquetar sin necesidad pasarlo como parametro en la clase
		tkinter.Label(fram,text='label prueba').pack() # Aqui tembien debe especificarse en donde sera empaquetado('fram') para que no asuma uno por defecto

raiz = tkinter.Tk()
raiz.geometry('500x400+500+310')
fram= tkinter.Frame(bg='red') # No es necesario especificar con cual empaquetar pero asumira uno por defecto en, este caso Tk('raiz')
fram.pack(fill= 'both', expand= 'True', pady=30, padx=10)
fram.config()
tkinter.Button(fram,text='BOTON').pack() # En este caso tuve que especificar que seria en el Frame('fram') ya que de lo contrario asumia que era raiz

ins = Test()
ins.Lab()
raiz.mainloop()
"""

# EJEMPLO 6.1 (Tkinter pero usando clase normal SIN Herencia >>Caso 2)
"""
class Test():

	def raiz(self):
		root= tkinter.Tk()
		tkinter.Button(text = 'BOTON').pack() # En un caso simple no es necesario especificar el parametro de empaquetamiento por que asume Tk('root') por defecto (No se sabe si puede asumir otro distinto por defecto)
		root.mainloop()

ins = Test()
ins.raiz()
"""


# EJEMPLO 7 ( HEREDANDO DE RAIZ(Tk) Tkinter y llamando metodos internamente) / Nota: Solo aplica para herencias de 'Tk'
"""
def fun(msg):
	print('MENSAJE:',msg)

class Test(tkinter.Tk):
	
#	def __init__(self):  # IMPORTANTE: Usar '__init__' con 'super()'' no funciono para llamar metodos internos ya que presenta irregularidades. 
#		self.boton()
#		super().__init__()
	

	def __init__(self, x,y, option = False): #sin embargo init sirve para declarar variables y recibir parametros directos e indirectos
		self.x = x
		self.yy = y
		self.z = 'ase :v' 
		#self.text_label = 0
		def fun_2(x):
			print ('This is secon function '+x)
		if option == True: # _init_ tambien se puede usar en este caso para crear estructiras simples siempre y cuando no impliquen llamadas a otros metodos
			self.text_label =1
		fun('Hello world') # Como se evidencia este '__init__' con 'super()' heredando de 'Tk' tambien permite llamar funciones
		fun_2('>:v') # Tambien permite llamar funciones internas del init
		super().__init__()

	def play(self): # por lo tanto en lugar de usar __init__ se utiliza un metodo normal auxiliar 
		self.boton()

	def boton(self):
		tkinter.Button(text='BOTON ' + self.x + self.yy + self.z).pack()
		if self.text_label == 1:
			self.cuadrotext()

	def cuadrotext(self):
		tkinter.Label(text='Label empaquetado exitosamente :V').pack()

equis= 'ola '
ye = 'que '
ins=Test(equis, ye, option= True)
ins.play()
ins.mainloop()
"""

# EJEMPLO 8 ( HEREDANDO DE RAIZ(Tk) EMPAQUETAMIENTO INTERNO ENTRE METODOS) 
class Test(tkinter.Tk):

#	def __init__(self):  
#		print('hola')
#		ins.geometry('300x300') El el '__init__' super().__init__()' de herencia de 'Tk' no permite ejecutar nisiquiera metodos de la herencia como geometry 
#		super().__init__()
	
	def play(self): # optimización de llamadas para no tener que hacerlo una por una en las instancia
		self.config()
		self.fram()
		self.boton()

	def config(self):
		ins.geometry('300x300')

	def fram(self):
		self.f=tkinter.Frame(bg='red')
		self.f.pack(fill= 'both' ,expand='True', padx=10, pady=12)

	def boton(self):
		tkinter.Button(self.f,text='BOTON').place(x= 50, y = 50)

ins=Test()
#ins.geometry('300x300')
#ins.config()
#ins.fram()
#ins.boton()
ins.play()

ins.mainloop()








