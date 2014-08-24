__author__ = 'Sergio'
# -*- coding: utf-8 -*-
# Proyecto hecho en python 2.7.x
archivo_texto = open('texto')
diccionario_palabras = dict()
diccionario_transiciones = dict()
caracteres_especiales = [' ', ',', '.', '', '+', '-', '=', '"', '/', '(', ')',';', ':']
palabra_anterior = '' #Acá declaré la palabra anterior fuera del "for" para que después a medida que pasen las lineas no la borre
for linea in archivo_texto:
    palabra_actual = ''

    for letra in linea.strip():
        if letra not in caracteres_especiales:
            palabra_actual += letra
        else:
            if palabra_actual not in diccionario_palabras:
                diccionario_palabras[palabra_actual] = 1
            else:
                diccionario_palabras[palabra_actual] += 1
            if palabra_actual not in diccionario_transiciones:
                diccionario_transiciones[palabra_actual] = dict() #Verifico que la palabra exista en el dict de transiciones
            if palabra_anterior != '':
                if palabra_anterior not in diccionario_transiciones[palabra_actual]:
                    diccionario_transiciones[palabra_actual][palabra_anterior] = 1 #Aca estoy creando un diccionario en otro diccionario
                else:
                    diccionario_transiciones[palabra_actual][palabra_anterior] += 1
            palabra_anterior = palabra_actual
            palabra_actual = ''


del diccionario_palabras['']
del diccionario_transiciones[''] #Bug del espacio vacío que elimino
archivo_texto.close()
del archivo_texto
archivo_datos = open('datos', 'w')
datos = ''
for i in diccionario_palabras:
    datos += (i + ':' + str(diccionario_palabras[i]) + '\n')
archivo_datos.write(datos)
del datos
del archivo_datos
archivo_transiciones = open('transiciones','w')
transiciones = ''
for palabra in diccionario_transiciones:
    transiciones += str(palabra) + ':' + str(diccionario_transiciones[palabra]) + '\n'
archivo_transiciones.write(transiciones)
archivo_transiciones.close()
del transiciones
del diccionario_transiciones
