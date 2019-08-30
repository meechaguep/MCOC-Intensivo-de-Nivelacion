import numpy as np


#intro to numerical computing with numpy

l1= [1,3,5,7]
l2= [9,11,13,15]

print l1 + l2 #agrega l2 a l1

suma_entre_elementos= []

for elemento1, elemento2 in zip(l1, l2):
	suma_entre_elementos.append(elemento1+elemento2)


print suma_entre_elementos #se suma cada elemento

gg = list(range(100))
print gg

gg_array = np.array(gg)
print gg_array #podemos ver la diferencia entre listas y arreglos y el tiempo en que lo procesa python

#codigo 2 

l11 = np.array([2,4,6,8])
l22 = np.array([10,12,14,16])

print l11.ndim #dimension l11

print l11.shape #cantidad de elementos de cada dimension
print("")

#operaciones matematicas
print l11*l22

print l11+100

print l22*100

print np.sin(l22)

print l11.dtype #tipo de arreglos

l33= np.array([2.3,4.2,5.,5]) #float64
print l33.dtype


limg = np.array([1j,5,2j]) #deberia indicar que es complejo
print limg.dtype 

lfloat32= np.array([1,2,3,4,5,6,7,8], dtype='float32')
print lfloat32.dtype #definimos float32


l2d = np.array([[22,33,44,55,66],[66,55,44,33,22]])

print l2d.size #tamano
print l2d.nbytes #bytes

#codigo 3

print l11[1:3] #posiciones 1 y 2, la ultima no la imprime
print l11[1:-1] #-1 es la ultima y -2 la antepenultima


print l11[::2] #cada dos pasos
print l11[:3]
print l11[-2:]

l11_lista= [2,4,6,8]

print l11_lista[0]  
print l11_lista[:1] #con listas

arreglo6x6_literal= np.arange(36).reshape(6,6)
print "veamos distintos puntos de esta matriz"
print arreglo6x6_literal
print arreglo6x6_literal[:,4]
print arreglo6x6_literal[1::2, :-1:2]
print arreglo6x6_literal[1::2, :3:2]
print arreglo6x6_literal[:, 1::2]

print arreglo6x6_literal[:,2] 
print arreglo6x6_literal[1::2, :-2:2]
print arreglo6x6_literal[4, :]
print arreglo6x6_literal[1::2, :4:2]


#codigo 4 

arreglo_paso100 = np.arange(100,100000000,100)

negat= np.array([-5,-4,-3,-2,-1,0,1,2,3])
print negat<0 #imprime true si es negativo


negat[negat<0] = 0 #convierte negativos a 0
print negat

print np.nonzero(negat)  #posiciones sin 0

laaa = np.array([1,2,3])
lbbb = np.array([1,3,5])


print laaa<lbbb #posicion donde laa es menor que lbb

print laaa
subset  = laaa[[0,2]]
print subset 
print subset.flags.owndata 

#5 ejercicio
ejercicio = np.arange(25).reshape(5,5)
print ejercicio%3==0

mod = ejercicio%3==0
print ejercicio[mod]

output = np.empty_like(ejercicio, dtype='float')
output.fill(np.nan) #asigno que sean nan
mask = ejercicio%3 == 0 
output[mask] = ejercicio[mask]


print output, ejercicio

#ultimo codigo
#dimensiones deben ser calculos entre dimensiones

print np.sum([1,np.nan,9]) #nan

print np.nansum([1,np.nan,9]) #ahora se usa nan
print ejercicio

ultimo = np.array([[2,2,4,4,5],[4,5,8,5,9]])
print ultimo

print "sumemos las columnas"
print np.sum(ultimo, axis=0) 

ultimoahora= np.arange(48).reshape(8,6) #nuevo arreglo 8x6
print ultimoahora.mean(axis=0).shape #promedios



print "gracias"

#ultimos minutos explica como usar archivos txt realizando distintos calcylos estadisticos, pero con un material para los de su clase
#no se pudo realizar pero se aprendio
