# -*- coding: utf8 -*-
#!/usr/bin/python
# Start
print (" ")
print ("*************************************")
print ("*    ¿Cual es tu tiempo vivido?     *")
print ("*************************************")
print (" ")
# Saludo
print ("Hola soy CHackA,")
print (" ")
# Description
print ("Este programa determina cuanto tiempo has vivido, a continuación sigue los pasos y vamos a ver el tiempo que has vivido:")
print (" ")
# CODE
nombre = input("Introduzca su nombre: ")
edad = int(input ("¿Cuantos años tienes?: "))
print (" ")
dias = edad * 365
horas = dias * 24
minutos = horas * 60
segundos = minutos * 60
print (nombre, "para tener %s años de edad... " % edad)
print ('has vivido %s dias,' % dias)
print ('tus horas vividas son %s,' % horas)
print ('y tus minutos vividos son %s.' % minutos)
# Despedida
print (" ")
print ("*************************************")
print ("*   Developer: CHackA               *")
print ("*************************************")
print (" ")
# End