#!/usr/bin/env python
# -*- coding: utf8 -*-
# Start
print (" ")
print ("**********************************************************")
print ("*  USO de Ejemplo de Clases Hereradas - CLASE MASCOTA    *")
print ("**********************************************************")
print (" ")
# Saludo
print ("Hola soy CHackA,")
print (" ")
# CODE

"""
    USO DE LA CLASE MASCOTA

"""
from CHackAP2ClaseMascotaHeredada import *

mi_primera_mascota = CHackAP2ClaseMascotaHeredada ("Fluffy", "Perro")

print(mi_primera_mascota)


"""
    USO DE LA CLASE PERRO
"""

bingo = Perro("Bingo", "Si")

print(bingo)
print(bingo.getPersigue())

rudolf = Perro("Rudolf", "No")
print(rudolf)
print(rudolf.getPersigue())

print(isinstance(bingo,Perro))
print(isinstance(mi_primera_mascota,Perro))
print(isinstance(bingo, CHackAP2ClaseMascotaHeredada))


# Despedida
print (" ")
print ("*************************************")
print ("*   Developer: CHackA               *")
print ("*************************************")
print (" ")
# End