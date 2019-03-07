# -*- coding: utf8 -*-
# Script para identificar los tipos de Operadores Aritmeticos
# Start
print (" ")
print ("****************************************************************")
print ("*        Identificar los tipos de Operadores Aritmeticos       *")
print ("****************************************************************")
print (" ")

#Tipo de Dato Entero
print ("************ ENTEROS **************")
entero1 = 7
entero2 = 5

# Operaciones aritmeticas
respuestaenterossuma = entero1+entero2
respuestaenterosresta = entero1-entero2
respuestaenterosmulti = entero1*entero2
respuestaenterosdivision = entero1/entero2
print ('Respuestas de numeros Enteros')
print ('La respuesta de la suma es: %s' %respuestaenterossuma)
print ('La respuesta de la resta es: %s' %respuestaenterosresta)
print ('La respuesta de la multiplicacion es: %s' %respuestaenterosmulti)
print ('La respuesta de la division es: %s' %respuestaenterosdivision)
print (" ")

# Tipo de Dato Real
print ("************ REALES **************")
real1 = 0.35
real2 = 0.29e-3

# Operaciones aritmeticas
respuestarealsuma = real1+real2
respuestarealresta = real1+real2
respuestarealsmulti = real1+real2
respuestaerealsdivision = real1+real2
print ('Respuestas de numeros Reales')
print ('La respuesta de la suma es: %s' %respuestarealsuma)
print ('La respuesta de la resta es: %s' %respuestarealresta)
print ('La respuesta de la multiplicacion es: %s' %respuestarealsmulti)
print ('La respuesta de la division es: %s' %respuestaerealsdivision)
print (" ")

# Imprime tipos cuales son los tipos de variables
print ('Tipos de Variales')
print (type(entero1))
print (type(real1))
print (" ")

# Tipo de dato "CADENAS"
print ("************ CADENAS **************")

# Comillas simples
print ("Tipo de Datos de Cadenas")
cadena1 = 'Texto entre comillas simples'
print cadena1
print type(cadena1)
print (" ")

# Comillas dobles
print ("Tipo de Cadena Comillas dobles")
cadena2 = "Texto entre comillas dobles"
print cadena2
print type(cadena2)
print (" ")

# Cadena con codigo escapes
print ("Tipo de Cadena con código de escapes")
cadenaesc = 'Texto entre \n\tcomillas simples'
print cadenaesc
print type(cadenaesc)
print (" ")

# Cadena multilinea
print ("Tipo de Cadena Multilineas")
cadenac = """Texto linea 1
linea 2
linea 3
linea 4
.
.
.
.
.
linea N
"""
print cadenac
print type (cadenac)
print (" ")

# Repetición de cadena
print ("Tipo de Cadena Repetición")
cadrep = "Cadena" * 3
print cadrep
print type (cadrep)
print (" ")

# Concatenacion de cadena
print ("Tipo de Cadena Concatenado")
nombre = "Jairo"
apellido = "Garcia"
nombre_completo = nombre + " " + apellido
print nombre_completo
print type (nombre_completo)
print (" ")

print "Tamano de cadena '", nombre_completo, "' es:", len(nombre_completo)
print (" ")

# acceder a rango de la cadena
print ("Acceder al rango de la cadena")
print nombre_completo[3:13]
print (" ")

# Tipo de Dato BOOLEANO
print ("************ BOOLEANOS **************")

print '\nTipos de datos booleanos'
print '========================\n'

# Tipos de datos booleanos
aT = True
print "El valor es Verdadero:", aT, ", el cual es de tipo", type(aT), "\n"

aF = False
print "El valor es Falso:", aF, ", el cual es de tipo", type(aF)

print '\nOperadores booleanos'
print '====================\n'

# Operadores booleanos
aAnd = True and False
print "SI es Verdadero Y Falso, entonces es:", aAnd, ", el cual es de tipo", type(aAnd), "\n"

aOr = True or False
print "SI es Verdadero O Falso, entonces es:", aOr, ", el cual es de tipo", type(aOr), "\n"

aNot = not True
print "Si NO es Verdadero, entonces es:", aNot, ", el cual es de tipo", type(aNot), "\n"
print (" ")

# Tipo de Dato CONJUNTO
print ("************ CONJUNTO **************")

"""
    Un conjunto, es una colección no ordenada y sin elementos repetidos.
    Los usos básicos de éstos incluyen verificación de pertenencia y
    eliminación de entradas duplicadas.
"""

# Crea un conjunto sin repetidos
print '\nCrea un conjunto sin repetidos'
print '========================\n'
plato = ['pastel', 'tequeno', 'papa', 'empanada', 'mandoca', 'queso']
print plato
print type(plato)
bebida = ['refresco', 'malta', 'jugo', 'cafe']
print bebida
print type(bebida)

# Establece un conjunto a una variable
print '\nEstablecer un conjunto de una variable'
print '========================\n'
para_comer = set(plato)
print para_comer
print type(para_comer)

para_tomar = set(bebida)
print para_tomar
print type(para_tomar)

# Ejemplo práctico de los condicionales
print '\nEjemplo práctico de los condicionales'
print '========================\n'
hay_tequeno = 'tequeno' in para_comer
hay_fresco = 'refresco' in para_tomar

print "\nTostadas A que Pipo!"
print "===================="

# valida si un elemento esta en el conjunto
print "Teneis tequeno?: ", 'tequeno' in para_comer

# valida si un elemento esta en el conjunto
print "Teneis pa tomar fresco?: ", 'refresco' in para_tomar

if (hay_tequeno and hay_fresco):
	print "Desayuno vergatario"
else:
    print "Desayuno ligero"
print (" ")

# Tipo de Dato LITAS
print ("************ LISTAS *********")

"""
   La lista en Python son variables que almacenan arrays,
   internamente cada posicion puede ser un tipo de datos distinto.
"""

# Coleccion ordenada / arreglos o vectores
l = [2, "tres", True, ["uno", 10]]
print l

# Accesar a un elemento especifico
l2 = l[1]
print l2

# Accesar a un elemento a una lista anidada
l3 = l[3][0]
print l3

# establecer nuevo valor de un elemento de lista
l[1] = 4
print l
l[1] = "tres"

# Obtener un rango de elemento especifico
l3 = l[0:3]
print l3

# Obtener un rango con soltos de elementos especificos
l4 = l[0:3:2]
print l4

l5 = l[1::2]
print l5
print (" ")

# Tipo de Dato TUPLAS
print ("************ TUPLAS *********")

"""
    Una tupla es una lista inmutable. Una tupla no puede
    modificarse de ningún modo después de su creación.
"""

# Ejemplo simple de tupla
tupla = 12345, 54321, 'hola!'

# Ejemplo de tuplas anidadas
otra = tupla, (1, 2, 3, 4, 5)

# operación asinacion de valores de una tupla en variables
x, y, z = tupla


print "\nDefiniendo conexion a BD MySql"
print "==============================\n"

conexion_bd = "127.0.0.1","root","123456","nomina",
print "Conexion tipica:", conexion_bd
print type(conexion_bd)
conexion_completa = conexion_bd, "3307","10",
print "\nConexion con parametros adicionales:", conexion_completa
print type(conexion_completa)

print "\n"

print "Acceder a la IP de la bd:",  conexion_completa[0][0]
print "Acceder al usuario de la bd:",  conexion_completa[0][1]
print "Acceder a la clave de la bd:",  conexion_completa[0][2]
print "Acceder al nombre de la bd:",  conexion_completa[0][3]
print "Acceder al puerto de conexion:", conexion_completa[1]
print "Acceder al tiempo de espera de conexion:", conexion_completa[2]

print "\nMas informacion sobre Mysql y Python http://mysql-python.sourceforge.net/MySQLdb.html"
print (" ")

# Tipo de Dato DICCIONARIO
print ("************ DICCIONARIO *********")

"""
    El diccionario, que define una relación
    uno a uno entre claves y valores.
"""

datos_basicos = {
    "nombres":"Leonardo Jose",
    "apellidos":"Caballero Garcia",
    "cedula":"14522590",
    "fecha_nacimiento":"03121980",
    "lugar_nacimiento":"Maracaibo, Zulia, Venezuela",
    "nacionalidad":"Venezolana",
    "estado_civil":"Complicado"
}

print "\nDetalle del diccionario"
print "=======================\n"

print "\nClaves del diccionario:", datos_basicos.keys()
print "\nValores del diccionario:", datos_basicos.values()
print "\nElementos del diccionario:", datos_basicos.items()


# Ejemplo practico de los diccionarios
print "\nInscripcion de Curso"
print "===================="

print "\nDatos de participante"
print "---------------------"

print "Cedula de identidad:", datos_basicos['cedula']
print "Nombre completo: " + datos_basicos['nombres'] + " " + datos_basicos['apellidos']

# Despedida
print (" ")
print ("*************************************")
print ("*   Developer: CHackA               *")
print ("*************************************")
print (" ")
# End