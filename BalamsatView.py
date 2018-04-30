
from tkinter import *
from tkinter import ttk
from tkinter import filedialog


import matplotlib 
import matplotlib.animation as an
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
from matplotlib import style


from cansat import ReadLog
from getBalamsatData import getTempData
from getBalamsatData import getPresData
from getBalamsatData import getAcData
from getBalamsatData import getOrData
from getBalamsatData import getAlData
from getBalamsatData import getVelData


matplotlib.use("TkAgg")
style.use("ggplot")


t = Figure(figsize = (5,5), dpi = 100)
a = t.add_subplot(211, facecolor = 'black')
#tempTab = t.add_subplot(222)
b = t.add_subplot(212, facecolor = 'black')
#presTab = t.add_subplot(224)

v = Figure(figsize = (5,5), dpi = 100)
ace = v.add_subplot(211,facecolor = 'black')
#aceTab = v.add_subplot(122)
vel = v.add_subplot(212, facecolor = 'black')
#velTab = v.add_subplot(224)

o = Figure(figsize = (5,5), dpi = 100)
ori = o.add_subplot(211,facecolor = 'black')
#oriTab = o.add_subplot(222)
altu = o.add_subplot(212, facecolor = 'black')
#altuTab = o.add_subplot(224)

def OpenFile():
		Filename = filedialog.askopenfilename(initialdir="/", filetypes =(("Text File", "*.log"),("All Files","*.*")),title = "Selecciona un log file.")
		return Filename

Filename = OpenFile()

def updateData(i):

	if Filename:
		logline = ReadLog(Filename)
		temperatura = getTempData(logline)
		presion = getPresData(logline)

		acx = getAcData(logline,0)
		acy = getAcData(logline,1)
		acz = getAcData(logline,2)

		velx = getVelData(acx)
		vely = getVelData(acy)
		velz = getVelData(acz)

		altura = getAlData(logline)
		orientacionx = getOrData(logline,0)
		orientaciony = getOrData(logline,1)
		orientacionz = getOrData(logline,2)
		
		#En este punto se limpian los plot antes de actualizarse
		a.clear()
		b.clear()
		a.plot(temperatura)
		a.title.set_text("Temperatura [°C]")
		b.plot(presion)
		b.title.set_text("Presion[m atm]")


		ace.clear()
		vel.clear()
		ace.plot(acx, label = "x")
		ace.plot(acy, label = "y")
		ace.plot(acz, label = "z")
		ace.title.set_text("Aceleracion [g]")
		ace.legend()
		vel.plot(velx, label = "x")
		vel.plot(vely, label = "y")
		vel.plot(velz, label = "z")
		vel.title.set_text("Velocidad [m/s]")
		vel.legend()

		ori.clear()
		altu.clear()
		ori.plot(orientacionx,label = "x")
		ori.plot(orientaciony, label = "y")
		ori.plot(orientacionz, label = "z")
		ori.title.set_text("Orientacion de campo magnético [Gauss]")
		ori.legend()

		altu.plot(altura)
		altu.title.set_text("Altura [msnm]")


class BalamsatView(Tk):

	def __init__(self, *args, **kwargs):
		Tk.__init__(self, *args, **kwargs)

		#Doy formato a la ventana
		#Tk.iconbitmap(self, default = "nombre.ico")
		if Filename:
			Tk.wm_title(self, "BalamSat now reading "+Filename)
		else:
			Tk.wm_title(self, "BalamSat")

		#Creo un contenedor
		root = Frame(self)
		root.pack(side = "top", fill = "both", expand = True)
		root.grid_rowconfigure(0, weight = 1)
		root.grid_columnconfigure(0, weight = 1)

		self.frames = {}

		#Agrego todas las vistas al diccionario llamado frames
		for F in (TempPres, AceVel, OrFrame):
			frame = F(root, self)
			self.frames[F] = frame
			frame.grid(row = 0, column = 0, sticky = "nsew")

		#Se muestra la ventana de inicio con un metodo definido abajo
		self.show_frame(TempPres)

	def show_frame(self, cont):
		#Este metodo pinta un vista segun queramos
		frame = self.frames[cont]
		frame.tkraise()

#Declaro una ventana de inicio sencilla
# class StartPage(Frame):
# 	def __init__(self, parent, controller):
# 		Frame.__init__(self, parent)
# 		initlabel = Label(self, text = "BalamsatView")
# 		initlabel.pack(pady = 10, padx = 10)

# 		boton2 = ttk.Button(self, text = "Graficos", command = lambda: controller.show_frame(TempPres))
# 		# boton2.grid(sticky = "ew")
# 		boton2.pack()


class TempPres(Frame):
	def __init__(self, parent, controller):
		Frame.__init__(self, parent)

		#Seccion de botones
		TempPresBoton = Button(self, text = "Temperatura y presion", command = lambda: controller.show_frame(TempPres))
		TempPresBoton.pack()
		AceVelBoton = Button(self, text = "Aceleracion y Velocidad", command = lambda: controller.show_frame(AceVel))
		AceVelBoton.pack()
		OrBoton = Button(self, text = "Orientacion y Altura", command = lambda: controller.show_frame(OrFrame))
		OrBoton.pack()

		canvas = FigureCanvasTkAgg(t, self)
		canvas.draw()
		canvas.get_tk_widget().pack(side = TOP, fill = BOTH, expand = True)

		toobar = NavigationToolbar2TkAgg(canvas, self)
		toobar.update()
		canvas._tkcanvas.pack(side = BOTTOM, fill = BOTH, expand = True)


class AceVel(Frame):
	def __init__(self, parent, controller):
		Frame.__init__(self, parent)

		#Botones
		TempPresBoton = Button(self, text = "Temperatura y presion", command = lambda: controller.show_frame(TempPres))
		TempPresBoton.pack()
		AceVelBoton = Button(self, text = "Aceleracion y Velocidad", command = lambda: controller.show_frame(AceVel))
		AceVelBoton.pack()
		OrBoton = Button(self, text = "Orientacion y Altura", command = lambda: controller.show_frame(OrFrame))
		OrBoton.pack()


		canvas = FigureCanvasTkAgg(v, self)
		canvas.draw()
		canvas.get_tk_widget().pack(side = BOTTOM, fill = BOTH, expand = True)

		toobar = NavigationToolbar2TkAgg(canvas, self)
		toobar.update()
		canvas._tkcanvas.pack(side = BOTTOM, fill = BOTH, expand = True)

class OrFrame(Frame):
	def __init__(self, parent, controller):
		Frame.__init__(self, parent)

		TempPresBoton = Button(self, text = "Temperatura y presion", command = lambda: controller.show_frame(TempPres))
		TempPresBoton.pack()
		AceVelBoton = Button(self, text = "Aceleracion y Velocidad", command = lambda: controller.show_frame(AceVel))
		AceVelBoton.pack()
		OrBoton = Button(self, text = "Orientacion y Altura", command = lambda: controller.show_frame(OrFrame))
		OrBoton.pack()


		canvas = FigureCanvasTkAgg(o, self)
		canvas.draw()
		canvas.get_tk_widget().pack(side = BOTTOM, fill = BOTH, expand = True)

		toobar = NavigationToolbar2TkAgg(canvas, self)
		toobar.update()
		canvas._tkcanvas.pack(side = BOTTOM, fill = BOTH, expand = True)



#Instancio a la ventana de inicio
app = BalamsatView()
#Se actualizan los plots cada 100 msegundos
ani = an.FuncAnimation(t, updateData, interval =  1000)
ani2 = an.FuncAnimation(v, updateData, interval =  1000)
ani3 = an.FuncAnimation(o, updateData, interval = 1000)
app.mainloop()