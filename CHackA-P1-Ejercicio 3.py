# -*- coding: utf8 -*-
#!/usr/bin/python
# Start
print (" ")
print ("********************************************************")
print ("* Ejemplos de Ejercicio 3 - FUNCIONES                  *")
print ("********************************************************")
print (" ")
# Saludo
print ("Hola soy CHackA,")
print (" ")
# Description
print ("Estos son los ejemplos del Ejercicio 3, investigar qué hacen las siguientes funciones predefinidas en Python :")
print (" ")
# CODE

# ----------------------
# Ejemplo abs(x)
print (" ---- Función abs(x) --- ")
print ("Ejemplo de abs(x), devuelve el valor absoluto de la variable.")
print ("Variables de Ejemplo:")
print (" ")
print "abs(-45) : ", abs(-45)
print "abs(100.12) : ", abs(100.12)
print "abs(119L) : ", abs(119L)
# ----------------------
print (" ")
# ----------------------
# Ejemplo chr(i)
print (" ---- Función chr(i) --- ")
print ("Ejemplo de chr(i), devuelve una cadena de un carácter cuyo código ASCII es el entero i. Por ejemplo, chr (97) devuelve la cadena 'a'. la variable debe estar en el rango [0..255].")
print ("Variables de Ejemplo: CHackA")
print (" ")
print "chr(67)  : ", chr(67)
print "chr(72)  : ", chr(72)
print "chr(97)  : ", chr(97)
print "chr(99)  : ", chr(99)
print "chr(107) : ", chr(107)
print "chr(65)  : ", chr(65)
# ----------------------
print (" ")
# ----------------------
# Ejemplo float()
print (" ---- Función float() --- ")
print ("Ejemplo de float(), convierte una cadena o número a coma flotante. Si el argumento es una cadena, debe contener una representación válida de un número en coma flotante, con espacio en blanco alrededor opcionalmente. ")
print ("Variables de Ejemplo:")
print (" ")
variable1 = 10
variable2 = 123.45
print "float(10) : ", float(variable1)
print "float(127.45) : ", float(variable2)
# ----------------------
print (" ")
# ----------------------
# Ejemplo len()
print (" ---- Función len() --- ")
print ("Ejemplo de len, es una función integrada que devuelve el número de caracteres de una cadena.")
print ("Variables de Ejemplo: El Hacking me gusta.")
variable21 = len("El Hacking me gusta.")
print ("La variable tiene %s caracteres." %variable21)
# ----------------------
print (" ")
# ----------------------
# Ejemplo str(v)
print (" ---- Función str(v) --- ")
print ("La función str(v) nos ayuda a convertir cualquier tipo de variable o varias variables a STRING.")
quetipoes1 = 32
quetipoes2 = 33.45
dato = str(quetipoes1)+str(quetipoes2)
print ("Función de str(v): %s" %dato)
# ----------------------
print (" ")
# ----------------------
# Ejemplo type(s)
print (" ---- Función type(s) --- ")
print ("A continuación ejemplos de tipos de variables:")
print (" ")
print ("Variable Entera (32):")
quetipoes1 = 32
print "Tipo de Variable: %s" % type (quetipoes1)
print ("Variable Flotante (32.45):")
quetipoes2 = 33.45
print "Tipo de Variable: %s" % type (quetipoes2)
print ("Variable Dic ('Nobre': 'ChackA', 'Edad': 32):")
dict = {'Nobre': 'ChackA', 'Edad': 32};
print "Tipo de Variable: %s" % type (dict)
# ----------------------
# Despedida
print (" ")
print ("*************************************")
print ("*   Developer: CHackA               *")
print ("*************************************")
print (" ")
# End