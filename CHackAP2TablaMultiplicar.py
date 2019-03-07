#!/usr/bin/env python
# -*- coding: utf8 -*-
# Start
print (" ")
print ("***************************************************")
print ("*    CLASE DE TABLA DE MULTIPLICAR                *")
print ("***************************************************")
print (" ")
# Saludo
print ("Hola soy CHackA,")
print (" ")
# Description
print ("Este es un objeto retonará la tabla de multiplicar de un número.")
print (" ")
# CODE

###############################################
#          CLASE MULTIPLICAR                  #
###############################################

class CHackAP2TablaMultiplicar():

    #Constructor de la clase Multiplicar
    def __init__(self,numero):
        self.numero = numero

    #Getters de la clase Multiplicar
    def getNumero(self):
        return ("que tabla quieres?" + str(self.numero))

    def mostrar_tabla(self):
        for i in range(0, 11):
            print(self.numero, "x", i, "=", self.numero * i)

# Despedida
print (" ")
print ("*************************************")
print ("*   Developer: CHackA               *")
print ("*************************************")
print (" ")
# End
