import tkinter as vent  # Esta vez para como vent para distinguir instancias(de clases) de funciones
import time


def fun(arg): # Nota: Aun no se determina si influye crear las funciones fuera del la interfaz grafica('Tk()')
	print(arg)
def fun2():
	#window.withdraw() # 'withdraw' permite ocultar la ventana
	"""Crear ventana secundaria"""
	window_2=vent.Toplevel() # 'Toplevel' crea ventanda secundarias dentro de la ventana raiz('Tk')
	window_2.geometry('80x80+100+60')
	vent.Label(window_2, text='Venetana Secundaria...').pack()
	"""Cierre de ventana Raiz y fin"""
	window.after(6000, window.destroy)
	#window.destroy() # 'destroy' permite terminar la ejecucion de la ventana definitivamente.

window = vent.Tk()

var= vent.StringVar()
var= 'Argumento'	

window.geometry('100x100+90+80') # Tamaño y posicion por defecto de la ventana raiz

vent.Label(window, text='VENTANA RAIZ').pack()
vent.Button(window, text='imprimir', command=lambda:fun(var)).pack() # Pasar agumentos con metodo 'lambda'
vent.Button(window, text='v.secundaria', command=fun2).pack()
vent.Button(window, text='cerrar', command=window.destroy).pack() # Tambien se pueden usar el comandos directos sin función


window.mainloop()