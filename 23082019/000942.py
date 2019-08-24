#hoy veremos while

#intento 1

suma=0 
inicio=100

while inicio < 200:
	suma+=inicio
	inicio+=1

print suma

#intento 2

lista = [15,14,13,12,11,10,9,8,7,6,5,4,3,2,1,0,-1,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15]
positivos=[]

contador=0
while lista[contador]>0:
	positivos.append(lista[contador])
	contador+=1

print "los mayores a 0 son"
print positivos	

#intento 3 

positivos2=[]
contador=0
while contador<len(positivos) and positivos[contador]>0:
	positivos2.append(positivos[contador])
	contador +=1
print positivos2 #esta es para evitar un error al pasarme de la lista

#intento 4

lista4 = lista
contador=0

for i in lista4:
	if i <=0:
		break
	contador+=i
print contador #imprime los positivos de la lista y para cuando ve un negativo

#intento 5
suma=0
i=0
azar=[656,64,466,64656,656.45,652,5,85,52114,-55,-7412,-99]

while True:
	suma+=azar[i]
	i+=1

	if azar[i]<=0:
		break

print suma