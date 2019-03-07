#!/usr/bin/env python
# -*- coding: utf8 -*-
# Start
print (" ")
print ("*************************************")
print ("*    Comparar números Complejos     *")
print ("*************************************")
print (" ")
# Saludo
print ("Hola soy CHackA,")
print (" ")
# Description
print ("Este programa hace la comparación de los números complejos;")
print (" ")
# CODE
# Comparacion entre números complejos

numero1 = int (input("Escribe el primer numero: "))
numero2 = int (input("Escribir el segundo numero: "))
print (" ")
if (numero1 >= numero2 and numero1 % numero2):
    print(numero1, "no es multiplo de", numero2)
elif (numero1 >=numero2 and numero1 % numero2 == 0):
    print (numero1, "es multiplo de", numero2)
elif (numero1 < numero2 and numero2 % numero1):
    print (numero2, "no es multiplo de", numero1)
else:
    print (numero2, "es multiplo de", numero1)

# Despedida
print (" ")
print ("*************************************")
print ("*   Developer: CHackA               *")
print ("*************************************")
print (" ")
# End
