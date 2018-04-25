import matplotlib.pyplot as plt

from getBalamsatData import altura
from getBalamsatData import temperatura
from getBalamsatData import presion
from getBalamsatData import aceleracion
from getBalamsatData import ax, ay, az 


def TempPlot(temperatura):
	plt.subplot(111)
	plt.plot(temperatura)
	plt.ylabel('Temperatura')
	plt.ylim((24,26))
	#plt.show()

temperaturePlot = TempPlot(temperatura)

print(type(temperaturePlot))
# plt.subplot(223)
# plt.plot(ay,'g')
# plt.plot(az,'b')
# plt.title('Velocidad en tres direcciones')
# plt.ylabel('Velocidad')
# plt.xlabel('Tiempo')

# plt.subplot(224)
# plt.plot(ox,'r', label = 'Grados en x')

# plt.plot(oy,'g', label = 'Grados en y')
# #plt.legend()
# plt.plot(oz,'b', label = 'Grados en z')
# #plt.legend()
# plt.title('Orientacion')
# plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0)
# #plt.plot(altura)

# plt.show()

