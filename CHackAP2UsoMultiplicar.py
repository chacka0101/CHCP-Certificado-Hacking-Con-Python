#!/usr/bin/env python
# -*- coding: utf8 -*-
# Start
print(" ")
print("**********************************************************")
print("*                USO DE MULTIPLICAR                      *")
print("**********************************************************")
print(" ")
# Saludo
print("Hola soy CHackA,")
print(" ")
# CODE

"""
    USO DE LA MULTIPLICACIÓN

"""

from CHackAP2TablaMultiplicar import *

# Formula para Multiplicar

print("Digite el número de la tabla de multiplicar quiere imprimir?: ")
numero = int(input())
print(" ")
print("Tabla del número:", numero)
print(" ")
objeto_tabla = CHackAP2TablaMultiplicar(numero)
objeto_tabla.mostrar_tabla()

# Despedida
print(" ")
print("*************************************")
print("*   Developer: CHackA               *")
print("*************************************")
print(" ")
# End
