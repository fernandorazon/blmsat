
from tkinter import *
from tkinter import ttk

import matplotlib 
import matplotlib.animation as an
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
from matplotlib import style



from getBalamsatData import temperatura
from getBalamsatData import presion

matplotlib.use("TkAgg")
style.use("ggplot")


class BalamsatView(Tk):

	def __init__(self, *args, **kwargs):
		Tk.__init__(self, *args, **kwargs)

		#Doy formato a la ventana
		#Tk.iconbitmap(self, default = "nombre.ico")
		Tk.wm_title(self, "BalamSat")

		#Creo un contenedor

		root = Frame(self)
		root.pack(side = "top", fill = "both", expand = True)

		root.grid_rowconfigure(0, weight = 1)
		root.grid_columnconfigure(0, weight = 1)

		self.frames = {}

		#Agrego todas las vistas al diccionario llamado frames
		for F in (StartPage, Dashboard):
			frame = F(root, self)
			self.frames[F] = frame
			frame.grid(row = 0, column = 0, sticky = "nsew")

		#Se muestra la ventana de inicio con un metodo definido abajo
		self.show_frame(StartPage)

	def show_frame(self, cont):
		#Este metodo pinta un vista segun queramos
		frame = self.frames[cont]
		frame.tkraise()

#Declaro una ventana de inicio sencilla

class StartPage(Frame):
	def __init__(self, parent, controller):
		Frame.__init__(self, parent)
		initlabel = Label(self, text = "Start Page")
		initlabel.pack(pady = 10, padx = 10)

		boton1 = ttk.Button(self, text = "Cargar", command = lambda: controller.show_frame(Dashboard))
		boton1.pack()


class Dashboard(Frame):
	def __init__(self, parent, controller):
		Frame.__init__(self, parent)

		# initlabel = Label(self, text = "Dashboard")
		# initlabel.grid(column =  sticky = "N", pady = 10, padx = 10)

		boton2 = Button(self, text = "Vista1", command = lambda: controller.show_frame(StartPage))
		boton2.grid(column = 1, row = 0)


		t = Figure(figsize = (5,5), dpi = 100)
		a = t.add_subplot(111)
		a.plot(temperatura)
		canvas = FigureCanvasTkAgg(t, self)
		canvas.draw()
		canvas.get_tk_widget().grid(column = 1, row = 1, sticky = "E")

		p = Figure(figsize = (5,5), dpi = 100)
		b = p.add_subplot(111)
		b.plot(presion)
		canvas1 = FigureCanvasTkAgg(p, self)
		canvas1.draw()
		canvas1.get_tk_widget().grid(column = 1, row = 2, sticky = "E")

		scroll = Scrollbar(self)
		scroll.grid(column = 3, sticky = "W")
		self.configure(yscrollcommand = scroll.set)  

		#Agrego un toolbar al canvas
		# toolbar = NavigationToolbar2TkAgg(canvas, self)
		# toolbar.update()
		# canvas._tkcanvas.pack()

		

		

#Instancio a la ventana de inicio

app = BalamsatView()
app.mainloop()