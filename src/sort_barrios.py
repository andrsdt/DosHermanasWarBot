# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 16:16:35 2020

@author: andres
"""
# Este sort_barrios.py se ejecuta manualmente cuando añadimos un barrio nuevo a barrios.txt
# y queremos crear un barrios_ordenados.txt por orden alfabético, que es el que utilizará el programa


def leer_archivo(fichero):
    with open (fichero, 'r', encoding = 'utf-8') as f:
        return ([linea for linea in f])   

barrios = leer_archivo('./data/barrios.txt')

def ordenar_barrios(barrios):
    return sorted([b for b in barrios])


def guardar_archivo(sin_ordenar,nuevo): #Utiliza la lista anterior para crear un txt ordenado
    with open (nuevo, 'w+', encoding = 'utf-8') as g:
        for barrio in ordenar_barrios(barrios):
            g.write(barrio)


if __name__ == '__main__':
    guardar_archivo('./data/barrios.txt', './data/barrios_ordenados.txt')