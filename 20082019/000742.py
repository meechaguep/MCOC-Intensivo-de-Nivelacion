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

#intento4

def multiplicacion_con_2_numeros(x,y):
	return numero2*numero1
print "ahora tenemos dos argumentos en una funcion"
numero1=4
numero2=2
print "tus numeros son:"
print numero1
print numero2


xy= multiplicacion_con_2_numeros(numero1,numero2)
print "la multiplicacion de estos es: "
print xy

#intento5
print "funcion some argument"
def funcion_someargument(some_argument):
	print some_argument
	print "excelent"

funcion_someargument(5)
