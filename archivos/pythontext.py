__author__ = 'Sergio'
# -*- coding: utf-8 -*-
# Proyecto hecho en python 2.7.x
archivo_texto = open('texto')
diccionario_palabras = dict()
for linea in archivo_texto:
    palabra_actual = ''
    for letra in linea.strip():
        if letra != ')' and letra != '(' and letra != '' and letra != ' ' and letra != '.' and letra != ',':
            palabra_actual += letra
        else:
            if palabra_actual not in diccionario_palabras:
                diccionario_palabras[palabra_actual] = 1
            else: diccionario_palabras[palabra_actual] += 1
            palabra_actual = ''
archivo_texto.close()
archivo_datos = open('datos', 'w')
datos = ''
for i in diccionario_palabras:
    datos += i + ':' + str(diccionario_palabras[i]) + '\n'
archivo_datos.write(datos)
