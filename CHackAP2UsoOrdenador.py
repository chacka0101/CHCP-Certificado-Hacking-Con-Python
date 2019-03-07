#!/usr/bin/env python
# -*- coding: utf8 -*-
# Start
print (" ")
print ("***************************************************")
print ("*    Ejemplo de USO DE ORDENADOR                  *")
print ("***************************************************")
print (" ")
# Saludo
print ("Hola soy CHackA,")
print (" ")
# Description
print ("Este programa llama a la clase Ordenador para poderlo Usar;")
print (" ")

from CHackAP2ClaseOrdenador import *

#Crear un raton nuevo
raton_dell = Raton("Dell","20DPIs", 50)

#Crear un teclado nuevo
teclado_base = Teclado("Base","Español", 30)

#Crear una tarjeta grafica
tarjeta_nvidia = TarjetaGrafica("NVIDIA", "9600", 100, 8, "V1.0")

#Creamos nuestro propio ordenador
ordenador_jairo = CHackAP2ClaseOrdenador(raton_dell,teclado_base,tarjeta_nvidia)

#Sacamos la informacion por pantalla
print(ordenador_jairo.obtenerInformacion())

# Despedida
print (" ")
print ("*************************************")
print ("*   Developer: CHackA               *")
print ("*************************************")
print (" ")
# End