__author__ = 'Sergio'
# -*- coding: utf-8 -*-
# Proyecto hecho en python 2.7.x
archivo_texto = open('texto')
diccionario_palabras = set()
diccionario_transiciones = dict()
caracteres_especiales = ['  ' ,' ', '-', '=', '"', '/', '(', ')',';', ':']
palabra_anterior = '' #Acá declaré la palabra anterior fuera del "for" para que después a medida que pasen las lineas no la borre


for linea in archivo_texto:

    for palabra_actual in linea.strip().split(' '):
        if palabra_actual != '':

            #diccionario_palabras.add(palabra_actual)
            if palabra_actual not in diccionario_transiciones:
                diccionario_transiciones[palabra_actual] = dict() #Verifico que la palabra exista en el dict de transiciones
            if palabra_anterior != '':
                if palabra_anterior not in diccionario_transiciones[palabra_actual]:
                    diccionario_transiciones[palabra_actual][palabra_anterior] = 1 #Aca estoy creando un diccionario en otro diccionario
                else:
                    diccionario_transiciones[palabra_actual][palabra_anterior] += 1
            palabra_anterior = palabra_actual
            palabra_actual = ''

archivo_texto.close()
'''Intento de matriz
matriz = [[None]]
for palabra in diccionario_palabras:
    matriz[0].append(palabra)
for palabra in range(1, len(matriz[0])):
    for p in (diccionario_transiciones[matriz[0][palabra]]):
        print p
print matriz


'''
archivo_transiciones = open('transiciones','w')
transiciones = ''
for palabra in diccionario_transiciones:
    transiciones += str(palabra) + ':' + str((diccionario_transiciones[palabra])) + '\n'
archivo_transiciones.write(transiciones)
archivo_transiciones.close()
del transiciones
del diccionario_transiciones #Borre variables

