#!/usr/bin/env python
# -*- coding: utf8 -*-
# Start
print (" ")
print ("***************************************************")
print ("*    Ejemplo Bucle WHILE y FOR Suma hasta 100     *")
print ("***************************************************")
print (" ")
# Saludo
print ("Hola soy CHackA,")
print (" ")
# Description
print ("Este programa hace una suma de todos los números desde el 1 hasta 100 con WHILE y con FOR;")
print (" ")
# CODE
# Ejemplo WHILE Y FOR


"""
Ejemplo de Bucle WHILE para suma hasta 100
"""

total_suma=0
i=0
while (i<100):
    total_suma+=i #total_suma = total_suma + i
    i+=1
print ("El total de la suma WHILE es:", total_suma)

"""
Ejemplo de Bucle FOR para suma hasta 100
"""
print (" ")
total_suma_for=0
for i in range(0,100,1):
    total_suma_for+=i
print ("El total de la suma FOR es:", total_suma_for)


# Despedida
print (" ")
print ("*************************************")
print ("*   Developer: CHackA               *")
print ("*************************************")
print (" ")
# End