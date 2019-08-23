#dia 5 uso del for

#intento 1

locales_de_comida_rapida= ["Mcdonnals","BurgerKing","Wendys","Carrito"]

#usaremos el for el cual recorrera la lista

for hambre in locales_de_comida_rapida:
	print hambre



# intento 2

vaquita=[1000,5000,500,2000,6000,800,4250]
reunido=0

for juntar in vaquita:
	reunido = reunido + juntar
	

print "se ha reunido: "
print reunido #deberia arrojar 19550

#intento 3

sucesion = list(range(1,51))
print sucesion #deberia imprimir los numeros del 1 al 50

#intento 4 

suma = 0
for num in range(10,16):
	suma += num
print suma #deberia imprimir 75

#intento 5

#veamos la funcion % que nos dara el resto
print "imprimira los restos de las dividiones:"
print (4%2)
print (8%4)
print (8%3)

#intento 6

#usemos el % en un for

suma_de_pares = 0
for num in range (1,51):
	if num % 2 ==0:
		suma_de_pares += num
	

print "la suma de los numeros pares que hay entre 1 y 50 es:"
print suma_de_pares

#intento 7 

suma_de_pares = 0
suma_de_impares=0
total=0

for num in range (1,51):
	if num % 2 ==0:
		suma_de_pares += num
		total += num
	else:
		 suma_de_impares += num
		 total += num
print "la lista es:"
print list(range(1,51))
print "la suma de sus numeros pares es:"
print suma_de_pares
print "la suma de sus numeros impares es:"
print suma_de_impares
print "la suma total es:"
print total 

print "eso es por hoy en cuanto a la nivelacion"

