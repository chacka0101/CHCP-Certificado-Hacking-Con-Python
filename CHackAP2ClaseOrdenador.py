#!/usr/bin/env python
# -*- coding: utf8 -*-
# Start
print (" ")
print ("***************************************************")
print ("*    Ejemplo de Clase Ordenador                   *")
print ("***************************************************")
print (" ")
# Saludo
print ("Hola soy CHackA,")
print (" ")
# Description
print ("Este programa para construir el ejemplo de una Clase Ordenador;")
print (" ")
# CODE

###############################################
#          CLASE ORDENADOR                    #
###############################################

class CHackAP2ClaseOrdenador():

    def __init__(self, raton, teclado, tarjeta_grafica):
        self.raton = raton
        self.teclado = teclado
        self.tarjeta_grafica = tarjeta_grafica

    def obtenerInformacion(self):
        return ("El ordenador tiene un raton de la marca " + str(self.raton.marca))


###############################################
#          SUB CLASE RATÓN                        #
###############################################
class Raton():

    def __init__(self,marca,precision,precio):
        self.marca = marca
        self.precision = precision
        self.precio = precio

    def mover(self):
        print ("El ratón se está moviendo")

###############################################
#          SUB CLASE TECLADO                      #
###############################################
class Teclado():

    def __init__(self,marca,lenguaje,precio):
        self.marca = marca
        self.lenguaje = lenguaje
        self.precio = precio

    def escribir(self):
        print ("El teclador está escribiendo")

###############################################
#          SUB CLASE TARJETA GRÁFICA              #
###############################################
class TarjetaGrafica():

    def __init__(self,marca,modelo,rendimiento,precio,version):
        self.marca = marca
        self.modelo = modelo
        self.precio = precio
        self.rendimiento = rendimiento
        self.version = version

    def rendimiento(self):
        print ("El rendimiento de esta tarjeta gráfica es de: " + str(rendimiento) + " sobre 10.")


# Despedida
print (" ")
print ("*************************************")
print ("*   Developer: CHackA               *")
print ("*************************************")
print (" ")
# End