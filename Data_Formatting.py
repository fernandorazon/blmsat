


from getBalamsatData import orientacionFloat

orientacionArchive = open("Orientacion.txt","w")

for i in orientacionFloat:
	orientacionArchive.write(str(i) + "\n")
