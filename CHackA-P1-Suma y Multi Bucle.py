# -*- coding: utf8 -*-
# Start
print (" ")
print ("********************************************************")
print ("* Suma y Multiplicación de Lista con Bucle             *")
print ("********************************************************")
print (" ")
# Saludo
print ("Hola soy CHackA,")
print (" ")
# Description
print ("Este programa suma y multiplica los valores de una lista con Bucle, a continuación sigue los pasos:")
print (" ")
# CODE
print ("Digita los 5 números que quieres sumar y multiplicar:,")
print (" ")
# Definir una lista
numero1 = int(input('Digite un número: '))
numero2 = int(input('Digite un número: '))
numero3 = int(input('Digite un número: '))
numero4 = int(input('Digite un número: '))
numero5 = int(input('Digite un número: '))

lista_numeros=[numero1,numero2,numero3,numero4]

# Variables
suma = 0
multi = 1

for i in lista_numeros:
    suma=suma+i
    multi=multi*i

print (" ")
print ("La suma de la lista es: %s" %suma)
print (" ")
print ("La multiplicacion de la lista es: %s" %multi)
print (" ")
# Despedida
print (" ")
print ("*************************************")
print ("*   Developer: CHackA               *")
print ("*************************************")
print (" ")
# End