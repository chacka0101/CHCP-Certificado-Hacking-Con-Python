# -*- coding: utf8 -*-
# Start
print (" ")
print ("********************************************************")
print ("* Suma y Multiplicación de Listas CON Funciones        *")
print ("********************************************************")
print (" ")
# Saludo
print ("Hola soy CHackA,")
print (" ")
# Description
print ("Este programa suma y multiplica los valores de las listas CON funciones, a continuación sigue los pasos:")
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

# Definir la funcion suma
def suma(lista):
    sum=0
    for i in lista:
        sum=sum+i
    return sum

# Definir la funcion multiplicacion
def multiplicacion(lista):
    multi=1
    for i in lista:
        multi=multi*i
    return multi
print (" ")
print ("La suma de la lista es: %s" %suma(lista_numeros))
print (" ")
print ("La multiplicacion de la lista es: %s" %multiplicacion(lista_numeros))
print (" ")
# Despedida
print (" ")
print ("*************************************")
print ("*   Developer: CHackA               *")
print ("*************************************")
print (" ")
# End