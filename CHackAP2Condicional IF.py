#!/usr/bin/env python
# -*- coding: utf8 -*-
# Start
print (" ")
print ("*************************************")
print ("*       Ejecicio Condicional IF     *")
print ("*************************************")
print (" ")
# Saludo
print ("Hola soy CHackA,")
print (" ")
# Description
print ("Este programa hace la comparación de varios números, vamos a comparar dos números;")
print (" ")
# CODE
# Comparacion entre varios numeros

numero1 = int (input("Escribe el primer numero: "))
numero2 = int (input("Escribir el segundo numero: "))
print (" ")
if (numero1 < numero2):
    print ("El número mayor es el ", numero2, " y  el número menor es el ", numero1)
elif (numero1 > numero2):
    print ("El número menor es el ", numero2, " y el número mayor es el ", numero1)
else:
    print ("Los dos numeros son iguales.")

# Despedida
print (" ")
print ("*************************************")
print ("*   Developer: CHackA               *")
print ("*************************************")
print (" ")
# End

