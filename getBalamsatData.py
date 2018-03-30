
from cansat import testLogLineString

import re
import string

def getData(testLogLineString):


	#En estas linea se genera una lista que elimina los \n \r y ; de los inicios de cada string
	testLogLineStringSplit = re.split('\r|\n|;',testLogLineString)

	#En este for se separa la informacion segun la bandera de su línea
	for i in testLogLineStringSplit:
		if i.startswith('T'):
			if i.startswith(string.digits,3):
				print(i)

		elif i.startswith('P'):
			#print(i)
			pass

		elif i.startswith('Ac'):
			#print(i)
			pass

		elif i.startswith('O'):
			#print(i)
			pass

		elif i.startswith('A'):
			#print(i)
			pass

#getData(testLogLineString)

a = 'asdfasdlkjañljd235'

#print(string.ascii_letters)