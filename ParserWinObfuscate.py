# -*- coding: utf-8 -*-
if 64 - 64: i11iIiiIii
import xml . etree . ElementTree as etree
import shutil , os , sys , time , win32ui
from colorama import init , Fore , Back , Style
init ( autoreset = True )
if 65 - 65: O0 / iIii1I11I1II1 % OoooooooOO - i1IIi
if ( os . name in ( 'ce' , 'nt' , 'dos' ) ) :
 os . system ( 'cls' )
 if 73 - 73: II111iiii
if len ( sys . argv ) < 2 :
 if 22 - 22: I1IiiI * Oo0Ooo / OoO0O00 . OoOoOO00 . o0oOOo0O0Ooo / I1ii11iIi11i
 print Fore . BLUE + "\n    _______ _     ____    ____  _  _        _ ____    _ _  _   _         "
 print Fore . BLUE + "   |__   __| |   |___ \  |___ \| || |      | |___ \  | | || | | |        "
 print Fore . BLUE + "      | |  | |__   __) |   __) | || |_ __ _| | __) | | | || |_| |__  ___ "
 print Fore . BLUE + "      | |  | '_ \ |__ <   |__ <|__   _/ _` | ||__ <  | |__   _| '_ \/ __|"
 print Fore . BLUE + "      | |  | | | |___) |  ___) |  | || (_| | |___) | | |  | | | |_) \__ \ "
 print Fore . BLUE + "      |_|  |_| |_|____/  |____/   |_| \__, |_|____/  |_|  |_| |_.__/|___/" 
 print Fore . BLUE + "                                       __/ |                             " 
 print Fore . BLUE + "                                      |___/ " 
 print Fore . BLUE + "\n|-----------------------------------------------------------------------------------------|"
 print "| Analizador de archivos .nessus                                                          |"
 print "|                                                                                         |"
 print "| USO:                                                                                    |"
 print "| 1: Tener en una carpeta todos los archivos .nessus que queramos juntar                  |"
 print "| 2: Abrir una consola de comandos y navegar a la misma carpeta de los archivos a juntar  |"
 print "| 3: Ejecutar 'python Parser.py'                                                          |"
 print "|                                theeaglelabs.com                                         |"
 print Fore . BLUE + "|-----------------------------------------------------------------------------------------|\n"
raw_input ( 'Pulse una tecla para continuar...' )
if 48 - 48: oO0o / OOooOOo / I11i / Ii1I
IiiIII111iI = 1
for IiII in os . listdir ( "." ) :
 if ".nessus" in IiII :
  print ( "Analizando..." , IiII )
  if IiiIII111iI :
   iI1Ii11111iIi = etree . parse ( IiII )
   i1i1II = iI1Ii11111iIi . find ( 'Report' )
   i1i1II . attrib [ 'name' ] = 'Reporte Final'
   IiiIII111iI = 0
  else :
   O0oo0OO0 = etree . parse ( IiII )
   for I1i1iiI1 in O0oo0OO0 . findall ( './/ReportHost' ) :
    iiIIIII1i1iI = i1i1II . find ( ".//ReportHost[@name='" + I1i1iiI1 . attrib [ 'name' ] + "']" )
    if not iiIIIII1i1iI :
     print "Agregar host: " + I1i1iiI1 . attrib [ 'name' ]
     i1i1II . append ( I1i1iiI1 )
    else :
     for o0oO0 in I1i1iiI1 . findall ( 'ReportItem' ) :
      if not iiIIIII1i1iI . find ( "ReportItem[@port='" + o0oO0 . attrib [ 'port' ] + "'][@pluginID='" + o0oO0 . attrib [ 'pluginID' ] + "']" ) :
       print "Agregando Hallazgos: " + o0oO0 . attrib [ 'port' ] + ":" + o0oO0 . attrib [ 'pluginID' ]
       iiIIIII1i1iI . append ( o0oO0 )
  print ( "Hecho ;)." )
  if 100 - 100: i11Ii11I1Ii1i
if "Reporte" in os . listdir ( "." ) :
 shutil . rmtree ( "Reporte" )
 if 67 - 67: iiI1iIiI . ooo0Oo0 * i1 - o0oOOo0O0Ooo * I1ii11iIi11i * iIii1I11I1II1
os . mkdir ( "Reporte" )
iI1Ii11111iIi . write ( "Reporte/ReporteFinal.nessus" , encoding = "utf-8" , xml_declaration = True )
win32ui . MessageBox ( "Finalizado" , "Parser" )
os . system ( "taskkill /im python.exe" )
sys . exit ( 0 ) # dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
