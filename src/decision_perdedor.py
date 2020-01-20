# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 00:57:36 2020

@author: andres
"""

from print_palabras import imprimir_texto, barrios
import random
import os.path
import pickle

# Intentar importar desde el fichero el dicc_descendiente, si no, utilizar el de abajo
# (Si es la primera vez que se ejecuta del programa, se creará el fichero, si no, se cargará el anterior y se irá actualizando)

if os.path.exists('./tmpdumps/dicc_descendente.p'):
    dicc_descendente = pickle.load( open( "./tmpdumps/dicc_descendente.p", "rb" ) )
else:
    dicc_descendente = dict(imprimir_texto(barrios))
        
    
def decision_ganador_perdedor():
    ganador = random.choice(list(dicc_descendente))
    perdedor = random.choice(list(dicc_descendente))
    
    while ganador == perdedor: # Para cuando se de el caso de que el random elija dos veces al mismo, cambiar el perdedor hasta que sea distinto
        perdedor = random.choice(list(dicc_descendente))
    
    del(dicc_descendente[perdedor]) # Elimina al perdedor del diccionario para que no vuelva a salir elegido
    
    return (ganador, perdedor), dicc_descendente