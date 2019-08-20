#dia 2 del curso de nivelacion
#funciones

def funcionimprimir():
	print "si lees esto es porque llamaste a la funcion"
	print "muy bien"

print "esto esta fuera de la funcion, si quieres ver que dice dentro llama a la funcion"

#intento 2

def funcionimprimir():
	print "si lees esto es porque llamaste a la funcion"
	print "muy bien"
print "esto esta fuera de la funcion, si quieres ver que dice dentro llama a la funcion"
print "llamare a la funcion"
funcionimprimir()

#intento3
print "veremos una funcion que me retorna el cuadrado de un numero x"
def cuadrado_del_numero(x):
	return x**2

numero=4
print "tu numero es:"
print numero

x2= cuadrado_del_numero(numero)
print "elevado al cuadrado es: "
print x2