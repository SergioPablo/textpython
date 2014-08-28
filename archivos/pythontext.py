__author__ = 'Sergio'
# -*- coding: utf-8 -*-
# Proyecto hecho en python 2.7.x
import cProfile
import random #Importo modulo random

def do_cprofile(func):
    def profiled_func(*args, **kwargs):
        profile = cProfile.Profile()
        try:
            profile.enable()
            result = func(*args, **kwargs)
            profile.disable()
            return result
        finally:
            profile.print_stats()
    return profiled_func


@do_cprofile

def crear_texto():

    archivo_texto = open('moby.txt') #Abrir archivo de texto
    diccionario_transiciones = dict() #Crear diccionario
    palabra_anterior = '' #Acá declaré la palabra anterior fuera del "for" para que después a medida que pasen las lineas no la borre


    for linea in archivo_texto:

        for palabra_actual in linea.strip().split(' '): #Separar las palabras de cada linea por espacio.

            if palabra_actual != '': #Verificar que la palabra que usaré no es un espacio vacío

                if len(diccionario_transiciones) == 0: #Si el diccionario no tiene palabras

                    diccionario_transiciones[palabra_actual] = list() #Agrego la palabra actual al diccionario y formo una lista
                    palabra_anterior = palabra_actual #Ahora la palabra actual pasará a ser la "Palabra anterior"

                elif len(diccionario_transiciones) == 1: #Si el diccionario tiene sólo una palabra

                    diccionario_transiciones[palabra_anterior].append(palabra_actual) #Agrego la palabra actual a la lista de la palabra anterior
                    diccionario_transiciones[palabra_actual] = list() #Agrego la palabra actual al diccionario con una lista
                    palabra_anterior = palabra_actual


                else: #Cuando ya hay más de 1 de una palabra en el diccionario

                    if palabra_anterior in diccionario_transiciones: #Si la palabra anterior ya está en diccionario
                        if palabra_anterior not in diccionario_transiciones[palabra_anterior]: #Si la palabra anterior no está en el diccionario de la palabra anterior entonces la agrego a la lista de la palabra anterior
                            diccionario_transiciones[palabra_anterior].append(palabra_actual)


                    else: #Sino está la palabra está se agrega (contrario de la condicional de arriba)
                        diccionario_transiciones[palabra_anterior] = list()
                        diccionario_transiciones[palabra_anterior].append(palabra_actual)


                    palabra_anterior = palabra_actual #Ahora la palabra actual pasará a ser la palabra anterior


    archivo_nuevo = open('archivo.txt','w') #Crea un archivo nuevo
    palabra_nueva = random.choice(list(diccionario_transiciones)) #Selecciona cualquier palabra del diccionario

    #Dentro de las condiciones del texto, aparece que debe tener de 4 a 10 parrafos de 4 a 10 lineas y que cada linea no debe tener más de 50 palabras.

    for parrafo in range(random.randint(4, 10)): #Elegir un número al azar de párrafos (Entre 4 y 10)

        for linea in range(random.randint(4, 10)): #Elegir un número al azar de lineas (entre 4 y 10)
            for palabra in range(15): #En este caso elegir 15 palabras por linea

                palabra_siguiente = random.choice(diccionario_transiciones[palabra_nueva]) #La palabra siguiente será un búsqueda al azar dentro de la lista de las posibles palabras siguientes de la palabra actual
                archivo_nuevo.write(palabra_nueva + ' ') #Escribo palabra por palabra agregando siempre un espacio
                palabra_nueva = palabra_siguiente #Ahora la palabra siguiente será la palabra nueva
            archivo_nuevo.write('\n') #Siempre que termina que se llega a la última palabra de la línea se agrega un salto de linea

        archivo_nuevo.write('\n') #Siempre que termine el párrafo agrego otra linea



    archivo_transiciones = open('transiciones','w')
    transiciones = ''
    for palabra in diccionario_transiciones:
        transiciones += str(palabra) + ':' + str(diccionario_transiciones[palabra]) + '\n'
    archivo_transiciones.write(transiciones)
    archivo_transiciones.close()
crear_texto()
