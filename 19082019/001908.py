print "comenzando la nivelacion"

name= "matias"
altura= 1.72
peso=75.

bmi= peso/ (altura**2)

print "tu bmi es: "
print bmi

if bmi <25:
	print name
	print "no estas con sobrepeso"
elif bmi==25:
	print name
	print "estas en el limite"
else:
	print name
	print "no estas con sobrepeso"
