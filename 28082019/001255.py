import numpy as np

a1= np.array([3,14,19])
print a1

a2= np.arange(41,56,3)#int,cada 3
print a2

a3=np.linspace(41,56,4)#float, 5 elementos
print a3

a4= a3.reshape(2,2)#lcambiamos a3 por una matriz de 2x2
print a4
print a3 #a3 sigue igual, a4 es una variable nueva

#intento 2 

print a3.size #cantidad de elementos
print a3.shape#nos muestra la composicion
print a3.dtype #indica el tipo de datos
print a3.itemsize #bits


print a4.size 
print a4.shape
print a4.dtype
print a4.itemsize

#intento 3

a5=a4*5 #multiplica la matriz
print a5

a6=np.array([4,3,2],dtype=np.int32)
print a6

