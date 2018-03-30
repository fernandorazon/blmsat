

#Adicionalmente, para poder tratar a nuestra ventana como un objeto con sus atributos como los deseamos
#Se puede declarar una clase heredera de la clase tk con los atributos deseados

from tkinter import *
from tkinter import ttk
#import cansat

class Ventana():
	def __init__(self):

		from cansat import testLogLineString

		root = Tk()                             #Esta es la instancia de una ventana
		root.geometry('500x500')                #Este atributo define el tamaño de la ventana           
		#root.configure(bg = 'gray')            #Este atriuto define el color del background
		root.title('Balamsat')   				#Este atributo define el titulo de la ventana

		T = Text(root)
		T.pack()
		#T.configure(bg = "gray")
		T.insert(END,testLogLineString)

		ttk.Button(root,text = 'Imprimir', command = root.destroy).pack()


		root.mainloop()

		

#Se puede definir a la funcion main como la forma de instanciar una ventana personalizada cuando se inicia la aplicacion

def main():
	mi_app = Ventana()
	return 0


#El atributo __name__ nos da acceso al nombre de un modulo, y permite a python conocer si un modulo es importado o no
if __name__ == '__main__':
	main()
