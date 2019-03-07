# -*- coding: utf8 -*-
#!/usr/bin/python
# Start
print (" ")
print ("********************************************************")
print ("* Ejemplos de Ejercicio 2 - METODOS                    *")
print ("********************************************************")
print (" ")
# Saludo
print ("Hola soy CHackA,")
print (" ")
# Description
print ("Estos son los ejemplos del Ejercicio 2, ¿Qué hacen los métodos aplicables a cadenas siguientes? :")
print (" ")
# CODE

# ----------------------
# Ejemplo capitalize()
print (" ---- Metodo capitalize --- ")
print ("Ejemplo de capitalize(), el cual establece la primera letra en mayuscula de la cadena: ")
print ("Cadena de Ejemplo: me gusta el hacking ético.")
str1 = "me gusta el hacking ético.";
str1.capitalize()
print "Resultado: ", str1.capitalize()
# ----------------------
print (" ")
# ----------------------
# Ejemplo isalnum()
print (" ---- Metodo isalnum --- ")
print ("Ejemplo de isalnum(), este método devuelve TRUE si todos los caracteres de la cadena son alfanuméricos y si hay algún carácter que no es alfanumerico, devuelve FALSE: ")
print ("Cadena de Ejemplo: ABCDE1")
str2 = "ABCDE1";  # No se pueden dejar espcaios
print "Resultado: ", str2.isalnum()
# ----------------------
print (" ")
# ----------------------
# Ejemplo islpha()
print (" ---- Metodo islpha --- ")
print ("Ejemplo de islpha(), este método devuelve TRUE si todos los caracteres de la cadena son alfabeticos y si hay algún carácter que no es alfabetico, devuelve FALSE: ")
print ("Cadena de Ejemplo: ABCDE1")
str3 = "ABCDE1";  # No se pueden dejar espcaios
print "Resultado: ", str3.isalpha()
# ----------------------
print (" ")
# ----------------------
# Ejemplo isupper()
print (" ---- Metodo isupper --- ")
print ("Ejemplo de isupper(), este método devuelve TRUE si todos los caracteres de la cadena son Mayusculas y si hay algún carácter que no es Mayuscula, devuelve FALSE: ")
print ("Cadena de Ejemplo: ABCDE1")
str4 = "ABCDE1";  # No se pueden dejar espcaios
print "Resultado: ", str4.isupper()
# ----------------------
print (" ")
# ----------------------
# Ejemplo lower()
print (" ---- Metodo lower --- ")
print ("Ejemplo de lower(), este método convierte todos los caracteres en Minusculas: ")
print ("Cadena de Ejemplo: Me Gusta El Hacking Ético")
str5 = "Me Gusta El Hacking Ético";  # No se pueden dejar espcaios
print "Resultado: ", str5.lower()
# ----------------------
print (" ")
# ----------------------
# Ejemplo rstrip()

print (" ---- Metodo rstrip --- ")
print ("Ejemplo de rstrip(), Este método devuelve una copia de la cadena, eliminando al final de la cadena el valor determinado, para este ejemplo es 2: ")
print ("Cadena de Ejemplo: Me Gusta El Hacking Ético!!!22222222222222222222222")
str6 = "Me Gusta El Hacking Ético!!!22222222222222222222222";
print "Resultado: ", str6.rstrip('2')

# ----------------------
# Despedida
print (" ")
print ("*************************************")
print ("*   Developer: CHackA               *")
print ("*************************************")
print (" ")
# End