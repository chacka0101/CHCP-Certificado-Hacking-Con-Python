#!/usr/bin/env python
# -*- coding: utf8 -*-
# Start
print (" ")
print ("***************************************************")
print ("*     CLASE HERERADA LIBRO - HACKERS  - COMIC     *")
print ("***************************************************")
print (" ")
# Saludo
print ("Hola soy CHackA,")
print (" ")
# Description
"""
Me han comentado estos hackers que tal vez necesiten una clase “Cómic” que hereda métodos y atributos de Libro, para poder administrar también sus cómics.
"""

print (" ")
# CODE

###############################################
#          CLASE LIBRO                        #
###############################################

class CHackAP2ClasLibroHackersEredada():

    #Constructor de la Clase Libro
    def __init__(self,nombreautor,nacionalidadautor,dedicatoria,titulolibro,tipodeletra,idiomalibro,nombreeditorial,nacionalidadeditorial,paginastotales,paginasleidas,dominiolibro,tecnicahacking):
        self.nombreautor = nombreautor
        self.nacionalidadautor = nacionalidadautor
        self.dedicatoria = dedicatoria
        self.titulolibro = titulolibro
        self.tipodeletra = tipodeletra
        self.idiomalibro = idiomalibro
        self.nombreeditorial = nombreeditorial
        self.nacionalidadeditorial = nacionalidadeditorial
        self.paginastotales = paginastotales
        self.paginasleidas = paginasleidas
        self.dominiolibro = dominiolibro
        self.tecnicahacking = tecnicahacking

    #Setters de la clase Mascota
    def setAutor(self,nombreautor,nacionalidadautor,dedictoria):
        self.nombreautor = nombreautor
        self.nacionalidadautor = nacionalidadautor
        self.dedicatoria = dedicatoria

    def setTitulo(self,titulolibro,tipoletra,idiomalibro):
        self.titulolibro = titulolibro
        self.tipodeletra = tipodeletra
        self.idiomalibro = idiomalibro

    def setEditorial(self, nombreeditorial,nacionalidadeditorial):
        self.nombreeditorial = nombreeditorial
        self.nacionalidadeditorial = nacionalidadeditorial

    def setPaginas(self,paginastotales,paginasleidas):
        self.paginastotales = paginastotales
        self.paginasleidas = paginasleidas

    def setDominio(self, dominiolibro, tecnicahacking):
        self.dominiolibro = dominiolibro
        self.tecnicahacking = tecnicahacking

    #Getters de la clase Mascota
    def getAutor(self):
        return ("Nombre del Autor: " + str(nombreautor))
        return ("Nacionalidad del Autor: " + str(nacionalidadautor))
        return ("El autor dedicará su libro a: " + str(dedicatoria))

    def getTitulo(self):
        return ("Titulo del Libro: " + str(titulolibro))
        return ("Tipo de Letra: " + str(tipoletra))
        return ("Idioma del libro: " + str(idiomalibro))

    def getEditorial(self):
        return ("Nombre de la Editorial: " + str(nombreeditorial))
        return ("Nacionalidad de la Editorial: " + str(nacionalidadeditorial))
        return ("Páginas totales del libro: " + str(paginastotales))
        return ("Cantidad de páginas leidas del libro: " + str(paginasleidas))

    def getDominio(self):
        return ("Dominio de conocimiento al que pertenece el libro: " + str(dominiolibro))
        return ("Técnica de Hackeo del Libro: " + str(tecnicahacking))

    #Metodo de la clase que sobreescribe el metodo print() que usamos normalmente
    def __str__(self):
        return ("%s es el titulo del libro y %s que es la técnica de Hacking utilizada." %(self.titulolibro, self.tecnicahacking))

###############################################
#          CLASE CÓMIC                     #
###############################################

class Comic(CHackAP2ClasLibroHackersEredada):

    def __init__(self,titulolibro,buscar_comic):
        CHackAP2ClaseMascotaHeredada.__init__(self,titulolibro,"Comic")
        self.buscar_comic = buscar_comic

    def setBuscar(self,buscar_comic):
        self.buscar_comic = buscar_comic

# Despedida
print (" ")
print ("*************************************")
print ("*   Developer: CHackA               *")
print ("*************************************")
print (" ")
# End