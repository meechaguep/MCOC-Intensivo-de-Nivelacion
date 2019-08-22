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