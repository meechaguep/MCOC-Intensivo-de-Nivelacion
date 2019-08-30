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

