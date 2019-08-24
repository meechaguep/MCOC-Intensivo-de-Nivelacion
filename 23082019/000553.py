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
print positivos2