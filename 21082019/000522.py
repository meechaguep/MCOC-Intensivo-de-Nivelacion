print "Este dia estudiaremos listas"

#intento 1

lista1= [14,21,3,-14,-21,-3]
print "la lista es:"
print lista1

#intento 2

print "agreguemos un numero a la lista"

lista1= [14,21,3,-14,-21,-3]
lista1.append(1313)
print lista1

#intento 3

print "ahora agreguemos una frase a esta lista de numeros"

lista1= [14,21,3,-14,-21,-3,1313] #las defino denuevo simplemente para hacer como codigos nuevos
lista1.append("hola numeros, soy un texto")
print lista1

#intento 4

print "ahora agreguemos una lista nueva dentro de la actual"

lista1= [14, 21, 3, -14, -21, -3, 1313, 'hola numeros, soy un texto']

lista1.append(["yo tambien soy texto",44,55,22])

print lista1

#intento5

#desde ahora llamare a la lista nomas, ya que se entiende que se siguen usando estos valores

print "eliminaremos ahora el ultimo parametro de la lista" #era una lista por lo que se cuenta como parametro de la lista inicial

lista1.pop()
print lista1
print "eliminaremos ahora el siguiente parametro"

lista1.pop()
print lista1

print "eliminaremos el siguiente"
lista1.pop()
print lista1

#intento 6

print "ahora veamos cual es el tercer valor de la lista"
print lista1[2] #le ponemos 2 porque comienza de 0

print "veamos el primer valor de la lista"
print lista1[0]

#intento 7

print "ahora cambiemos el primer y ultimo valor de la lista"

lista1[0]= "soy el 14"
lista1[5]= "y yo el -3"

print lista1