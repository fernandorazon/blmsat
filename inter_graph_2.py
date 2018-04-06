

#Adicionalmente, para poder tratar a nuestra ventana como un objeto con sus atributos como los deseamos
#Se puede declarar una clase heredera de la clase tk con los atributos deseados

from tkinter import *
from tkinter import ttk

from cansat import testLogLineString
from getBalamsatData import aceleracion as ac

#Hago los datos de ac presentables correctamente

acdata = []
for i, line in enumerate(ac,0):
	acdata.append(str(ac[0])+' '+str(ac[1])+' 'str(ac[2])+'\n')



#import cansat

class Ventana():
	def __init__(self):

		

		root = Tk()                             #Esta es la instancia de una ventana
		#root.geometry('500x500')                #Este atributo define el tamaño de la ventana           
		root.title('Balamsat')   				#Este atributo define el titulo de la ventana

		#Agrego un label con los datos obtenidos de la aceleracion
		T = Label(root, text = acdata)
		T.pack(side = LEFT)
		#ttk.Button(root,text = 'Imprimir', command = root.destroy).pack()

		#Agrego una tabla de aceleracion 



		root.mainloop()



		

#Se puede definir a la funcion main como la forma de instanciar una ventana personalizada cuando se inicia la aplicacion

def main():
	mi_app = Ventana()
	return 0


#El atributo __name__ nos da acceso al nombre de un modulo, y permite a python conocer si un modulo es importado o no
if __name__ == '__main__':
	main()
