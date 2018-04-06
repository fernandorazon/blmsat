
from cansat import testLogLineString

import re
import string

temperatura = []
presion = []
aceleracion = []
orientacion = []
a = []

#Esta funcion valida que los datos del documento sean numeros
#Si no lo son retorna un string Nan
#NOTA IMPORTANTE: Solo funciona en las banderas T P y A debido al formato con que estas llegan

def validateData(i):

	try:
		value = re.split('=|Pa| metros',i)
		values = float(value[1])

	except ValueError as e:
		values = 'Nan'

	except IndexError as e:
		values = 'No data'

	return values

def getData(testLogLineString):



	#En estas linea se genera una lista que elimina los \n \r y ; de los inicios de cada string
	testLogLineStringSplit = re.split('\r|\n|;',testLogLineString)

	#En este for se separa la informacion segun la bandera de su línea
	#Por buena practica, se prefiere el if elif que el switch 
	for i in testLogLineStringSplit:

		if i.startswith('T'):
			temperatura.append(validateData(i))

		elif i.startswith('P'):
			presion.append(validateData(i))
			

			
		elif i.startswith('Ac'):
			#Se separa cada valor segun el formato en el que venga y se guardan esos valores en acvalues

			#acvalues = re.split(' |:Xa=|:Ya=|:Za=|;',i)
			acvalues = re.split(' Xa= | Ya= | Za= ',i)

			#Valido que el formato de la linea sea el correcto, a partir de la longitud de acvalues
			if len(acvalues) == 4:
				try:
					aceleracion.append([float(acvalues[1]),float(acvalues[2]),float(acvalues[3])])
				except ValueError as e:
					aceleracion.append(['Nan','Nan','Nan'])
				except IndexError as e:
					aceleracion.append(['No data','No data','No data'])
			


		elif i.startswith('O'):

			#orvalues = re.split(':x=|:y=|:z=|;',i)
			orvalues = re.split('x: | y: | z: ',i)
			
			if len(orvalues) >= 4:
				try:
					orientacion.append([float(orvalues[1]),float(orvalues[2]),float(orvalues[3])])
				except ValueError as e:
					orientacion.append(['Nan','Nan','Nan'])

			else:
				orientacion.append(['No data','No data','No data'])



		elif i.startswith('A'):

			a.append(validateData(i))

		else:
			pass

	#print(len(temperatura))
	#print(len(aceleracion))
	#print(len(orientacion))
	#print(len(presion))
	#print(len(a))
	
#Aqui se manda a llamar a la funcion 
getData(testLogLineString)