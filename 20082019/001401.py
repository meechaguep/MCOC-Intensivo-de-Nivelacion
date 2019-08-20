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

#intento6

print "veamos tu IMC"

name= "matias"
altura= 1.72
peso= 75.

name2= "vicente"
altura2= 1.73
peso2= 84.

name3= "anibal"
altura3= 1.80002
peso3=90.

name4="martin"
altura4=1.82
peso4=72.

def calculo_imc(nombre,altura,peso):
	bmi= peso/(altura**2)
	print "tu imc es:"
	print bmi

	if bmi<25:
		return nombre + "  no estas con sobrepeso"
	else:
		return nombre + "  estas con sobrepeso muchacho"

bmi_1= calculo_imc(name,altura,peso)
print bmi_1
bmi_2= calculo_imc(name2,altura2,peso2)
print bmi_2
bmi_3= calculo_imc(name3,altura3,peso3)
print bmi_3
bmi_4= calculo_imc(name4,altura4,peso4)
print bmi_4

print "terminamos con este tutorial"

