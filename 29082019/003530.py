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

