#diccionarios

goles_1era_division={} 

goles_1era_division["Esteban Paredes"]=215
goles_1era_division["Milovan"]= 2
goles_1era_division["herrera"]=-215

print goles_1era_division #imprime el diccionario
#lo siguiente imprime valores del diccionario
print goles_1era_division["Esteban Paredes"]
print goles_1era_division["Milovan"]
print goles_1era_division["herrera"]


#intento 2

print "puede ser en base a numeros"

goles_1era_division[7]=215
print goles_1era_division[7]

#intento 3
print ""

print "veamos los valores del diccionario"

for jugador,goles in goles_1era_division.items():
	print "El jugador es:", jugador #veo la llave
	print "Sus goles son:", goles #veo el valor de esa llave


