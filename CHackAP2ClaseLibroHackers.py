#!/usr/bin/env python
# -*- coding: utf8 -*-
# Start
print (" ")
print ("***************************************************")
print ("*         CLASE LIBRO - HACKERS                   *")
print ("***************************************************")
print (" ")
# Saludo
print ("Hola soy CHackA,")
print (" ")
# Description
"""
Un grupo de hackers quiere crear una clase “Libro” que tenga atributos y métodos para características como
título, autor, editorial, páginas totales, páginas leídas para tener almacenados todos los libros de
los que disponen en su base. Ayúdales a administrar su propia biblioteca personal.
"""

print (" ")
# CODE

###############################################
#          CLASE LIBRO                        #
###############################################

class CHackAP2ClaseLibroHackers():

    def __init__(self,Autor,Titulo,Editorial,Paginas,Dominio):
        self.Autor = Autor
        self.Titulo = Titulo
        self.Editorial = Editorial
        self.Paginas = Paginas
        self.Dominio = Dominio

    def obtenerInformacion(self):
        return ("El Libro está leido hasta la página" + str(self.paginasleidas))


###############################################
#          SUB CLASE AUTOR                    #
###############################################
class Autor():

    def __init__(self,nombreautor,nacionalidadautor,didicatoria):
        self.nombreautor = nombreautor
        self.nacionalidadautor = nacionalidadautor
        self.dedicatoria = dedicatoria

    def mover(self):
        print ("El autor escribe")

###############################################
#          SUB CLASE TITULO                   #
###############################################
class Titulo():

    def __init__(self,titulolibro,tipoletra,idiomalibro):
        self.titulolibro = titulolibro
        self.tipodeletra = tipodeletra
        self.idiomalibro = idiomalibro

    def escribir(self):
        print ("El Libro siempre tiene un Titulo")

###############################################
#          SUB CLASE EDITORIAL                #
###############################################
class Editorial():

    def __init__(self,nombreeditorial,nacionalidadeditorial):
        self.nombreeditorial = nombreeditorial
        self.nacionalidadeditorial = nacionalidadeditorial

    def escribir(self):
        print ("La Editorial es la que imprime el libro")

###############################################
#          SUB CLASE PAGINAS                  #
###############################################
class Paginas():

    def __init__(self,paginastotales,paginasleidas):
            self.paginastotales = paginastotales
            self.paginasleidas = paginasleidas

    def escribir(self):
         print("Estado de páginas del libro")

###############################################
#          SUB CLASE DOMINIO                  #
###############################################
class Dominio():

    def __init__(self,dominiolibro,tecnicahacking):
            self.dominiolibro = dominiolibro
            self.tecnicahacking = tecnicahacking

    def mover(self):
         print("Selecciona la catergodia o dominio del Libro")

# Despedida
print (" ")
print ("*************************************")
print ("*   Developer: CHackA               *")
print ("*************************************")
print (" ")
# End