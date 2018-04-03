
#Cansat.py
#Programa que recoge los datos de un .log


def ReadLog():

	#Declaro variables auxiliares locales
	a = ""
	testLogLinesHex = ""
	count = 0
	testLogLines = []

	#Se recorre todo el documento para conocer el número de líneas que tiene
	for line in open("record1.log").readlines():
		count += 1

	testLog = open("record1.log","r")
	#Este for recorre todo el documento desde la linea desde la línea 3 (donde empieza la información)
	for i, line in enumerate(testLog,1):
		if i in range(3,count):
			a = line.split(',RECV,')
			testLogLines.append(a[1]) #testLogLines es la informacion en hexadecimal separada


	#Este for pasa de la lista testLogLines, a formar un solo string, eliminando los saltos de línea y sumando cada string
	for i in testLogLines:
		a = i.rstrip("\n")
		testLogLinesHex += a

	#Por ultimo se convierte de string en HEX a string en ASCII de modo que se obtiene la información del log
	testLogLineString = bytearray.fromhex(testLogLinesHex).decode()
	#print(testLogLineString)

	return testLogLineString

#Aquí mando llamar a la funcion que se ejecuta sobre el log de prueba
testLogLineString = ReadLog()
