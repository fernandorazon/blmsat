
from cansat import testLogLineString

import re
import string

temperatura = []
presion = []
aceleracion = []
ax = []
ay = []
az = []
orientacion = []
ox =[]
oy = []
oz =[]
a = []

#Esta funcion valida que los datos del documento sean numeros
#Si no lo son retorna un string Nan
#NOTA IMPORTANTE: Solo funciona en las banderas T P y A debido al formato con que estas llegan
def validateData(i):

	try:
		value = re.split('=|Pa| metros',i)
		values = float(value[1])

	except ValueError as e:
		values = 0

	except IndexError as e:
		values = 0

	return values

def getTempData(testLogLineString):
	#En estas linea se genera una lista que elimina los \n \r y ; de los inicios de cada string
	testLogLineStringSplit = re.split('\r|\n|;',testLogLineString)
	#En este for se separa la informacion segun la bandera de su línea 
	for i in testLogLineStringSplit:
		if i.startswith('T'):
			temperatura.append(validateData(i))
	return temperatura

def getPresData(testLogLineString):
	testLogLineStringSplit = re.split('\r|\n|;',testLogLineString)
	for i in testLogLineStringSplit:
		if i.startswith('P'):
			presion.append(validateData(i))
	return presion

def getAcData(testLogLineString):
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
					#aceleracion.append(['Nan','Nan','Nan'])
					pass
				except IndexError as e:
					#aceleracion.append(['No data','No data','No data'])
					pass
	return aceleracion

def getAlData(testLogLineString):
	testLogLineStringSplit = re.split('\r|\n|;',testLogLineString)
	for i in testLogLineStringSplit:
		if i.startswith('A'):
			a.append(validateData(i))
	return a

def getOrData(testLogLineString):
	testLogLineStringSplit = re.split('\r|\n|;',testLogLineString)
	for i in testLogLineStringSplit:
		if i.startswith('O'):
			orvalues = re.split(':x=|:y=|:z=|;',i)
			#orvalues = re.split('x: | y: | z: ',i)
			
			if len(orvalues) >= 4:
				try:
					orientacion.append([float(orvalues[1]),float(orvalues[2]),float(orvalues[3])])
				except ValueError as e:
					orientacion.append(['Nan','Nan','Nan'])

			else:
				orientacion.append(['No data','No data','No data'])

	return orientacion

temperatura = getTempData(testLogLineString)
presion = getPresData(testLogLineString)
aceleracion = getAcData(testLogLineString)
orientacion = getOrData(testLogLineString)
altura = getAlData(testLogLineString)

for i in aceleracion:
	for j in i:

		ax.append(i[0])
		ay.append(i[1])
		az.append(i[2])

for i in orientacion:
	for j in i:
		ox.append(i[0])
		oy.append(i[1])
		oz.append(i[2])


print(ox)


print(aceleracion)
