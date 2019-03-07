#!/usr/bin/env python
# -*- coding: utf8 -*-
# Start
print (" ")
print ("***************************************************")
print ("*  Ejemplo de Clases Hereradas - CLASE MASCOTA    *")
print ("***************************************************")
print (" ")
# Saludo
print ("Hola soy CHackA,")
print (" ")
# Description
"""
    CLASE MASCOTA

    Se trata de un ejemplo donde trabajaremos con herencia de clases.

    Vamos a trabajar con las clases Mascota, Perro, Gato. Las clases perro y gato son clases que heredan
    de la clase Mascota, que actúa como "clase madre".

"""

###############################################
#          CLASE MASCOTA                      #
###############################################

class CHackAP2ClaseMascotaHeredada():

    #Constructor de la clase Mascota
    def __init__(self,nombre,especie):
        self.nombre = nombre
        self.especie = especie

    #Setters de la clase Mascota
    def setNombre(self,nombre_nuevo):
        self.nombre = nombre_nuevo

    def setEspecie(self,especie_nueva):
        self.especie = especie_nueva

    #Getters de la clase Mascota
    def getNombre(self):
        return ("Mi nombre es: " + str(nombre))

    def getEspecie(self):
        return ("Mi especie es: " + str(especie))

    #Metodo de la clase que sobreescribe el metodo print() que usamos normalmente
    def __str__(self):
        return ("%s es un %s" %(self.nombre, self.especie))

###############################################
#          CLASE PERRO                      #
###############################################

class Perro(CHackAP2ClaseMascotaHeredada):

    def __init__(self,nombre,perseguir_gatos):
        CHackAP2ClaseMascotaHeredada.__init__(self,nombre,"Perro")
        self.perseguir_gatos = perseguir_gatos

    def setPersigue(self,perseguir_gatos):
        self.perseguir_gatos = perseguir_gatos

    def getPersigue(self):
        return ("¿Le gusta al perro " + str(self.nombre) + " perseguir gatos?: " + str(self.perseguir_gatos))

    #Metodo de la clase que sobreescribe el metodo print() que usamos normalmente
    def __str__(self):
        return ("%s es un %s" %(self.nombre, self.especie))

# Despedida
print (" ")
print ("*************************************")
print ("*   Developer: CHackA               *")
print ("*************************************")
print (" ")
# End