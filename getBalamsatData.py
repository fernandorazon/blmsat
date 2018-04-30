
from cansat import ReadLog
import re
import math as m

temperatura = []
presion = []
aceleracion = []
ax = []
ay = []
az = []
orientacion = []
orientacionFloat =[]
oy = []
oz =[]
alt = []
cont = 0

#Esta funcion valida que los datos del documento sean numeros
#Si no lo son retorna un string Nan
#NOTA IMPORTANTE: Solo funciona en las banderas T P y A debido al formato con que estas llegan
def validateData(i):

	try:
		value = re.split('=',i)
		values = float(value[1])

	except ValueError as e:
		values = 'Nan'

	except IndexError as e:
		values = 'No data'

	return values

def getTempData(testLogLineString):
	temperaturaFloat = []
	temperatura = []
	cont = 0
	#En estas linea se genera una lista que elimina los \n \r y ; de los inicios de cada string
	testLogLineStringSplit = re.split('\r|\n|;',testLogLineString)
	#En este for se separa la informacion segun la bandera de su línea 
	for i in testLogLineStringSplit:
		if i.startswith('T'):
			temperatura.append(validateData(i))

	for i in temperatura:
		if isinstance(i, float):
			temperaturaFloat.append(i)

	return temperaturaFloat

def getPresData(testLogLineString):
	presionFloat = []
	presion = []
	testLogLineStringSplit = re.split('\r|\n|;',testLogLineString)
	for i in testLogLineStringSplit:
		if i.startswith('P'):
			presion.append(validateData(i))

	for i in presion:
		if isinstance(i, float):
			i = i/100
			presionFloat.append(i)
	return presionFloat

def getAcData(testLogLineString, n):
	aceleracion = []
	acFloat = []
	testLogLineStringSplit = re.split('\r|\n|;',testLogLineString)
	for i in testLogLineStringSplit:
		if i.startswith('Ac'):
			#Se separa cada valor segun el formato en el que venga y se guardan esos valores en acvalues
			acvalues = re.split(' |:Xa=|:Ya=|:Za=|;',i)
			#acvalues = re.split(' Xa= | Ya= | Za= ',i)

			#Valido que el formato de la linea sea el correcto, a partir de la longitud de acvalues
			if len(acvalues) == 4:
				try:
					aceleracion.append([float(acvalues[1]),float(acvalues[2]),float(acvalues[3])])
				except ValueError as e:
					aceleracion.append(['Nan','Nan','Nan'])
				except IndexError as e:
					aceleracion.append(['No data','No data','No data'])

	for i in aceleracion:
		if isinstance(i[0], float):
			acFloat.append(i[n])

	return acFloat

def getVelData(aceleracion):
	vi = 0
	velocidades = []
	for i in aceleracion:
		vx = vi + (i*50e-3*9.81)
		vi = vx
		velocidades.append(vx)

	return velocidades


def getAlData(testLogLineString):
	alt = []
	altFloat = []
	testLogLineStringSplit = re.split('\r|\n|;',testLogLineString)
	for i in testLogLineStringSplit:
		if i.startswith('Al'):
			try:
				value = re.split('=',i)
				if len(value) == 2 and float(value[1])>1000:
					alt.append(float(value[1]))

			except ValueError as e:
				alt.append('Nan')

			except IndexError as e:
				alt.append('Nan')

	for i in alt:
		if isinstance(i, float):
			altFloat.append(i)

	return altFloat

def getOrData(testLogLineString,n):
	orientacion = []
	orientacionFloatx =[]
	orientacionFloaty = []
	orientacionFloatz = []

	testLogLineStringSplit = re.split('\r|\n|;',testLogLineString)
	for i in testLogLineStringSplit:
		if i.startswith('O'):
			orvalues = re.split(':x=|:y=|:z=|;',i)
			#orvalues = re.split('x: | y: | z: ',i)
			
			if len(orvalues) >= 4:
				try:
					if float(orvalues[1]) < 1 and float(orvalues[2]) < 1 and float(orvalues[3]) < 1:
						orientacion.append([float(orvalues[1]),float(orvalues[2]),float(orvalues[3])])
				except ValueError as e:
					orientacion.append(['Nan','Nan','Nan'])

			else:
				orientacion.append(['No data','No data','No data'])

	for i in orientacion:
		if isinstance(i[0],float):
			orientacionFloatx.append(i[n])

	return orientacionFloatx




