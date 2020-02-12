# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 16:25:27 2020

@author: andres
"""

from twitter_api import api
from decision_perdedor import decision_ganador_perdedor, dicc_descendente
from print_palabras import tachar_barrio
from modificadores import mod_conquista, filtros_personalizados_perdedor, filtros_personalizados_ganador
import os
import time
import random
import shutil
import pickle


# Si es la primera vez que se ejecuta el programa, que en updated_img.png esté todo sin tachar
if not os.path.exists('./tmpdumps/dicc_descendente.p'):   
    shutil.copy('./out/imprimir_texto.png' , './out/subir/updated_img.png')
    
    
imagen = './out/subir/updated_img.png'
    
while len(dicc_descendente)>=0:
    
    (ganador, perdedor), dicc_descendente = decision_ganador_perdedor()
    
    # Estas dos funciones sirven para transformar el barrio en hashtag: Ciudad Blanca --> #CiudadBlanca
    tagganador = '#'+ (ganador.strip()).replace(' ','')
    tagperdedor = '#'+ (perdedor.strip()).replace(' ','')
    
    # En el tweet se utilizará una frase personalizada en el caso de que la haya para dicho barrio
    perdedor_mod = filtros_personalizados_perdedor(perdedor)
    ganador_mod = filtros_personalizados_ganador(ganador)


    if len(dicc_descendente) > 2: # Si quedan más de dos barrios, el tweet es del tipo:
        tweet = ('{} {} {}, ¡quedan {} barrios!\n\n{} {}'.format(ganador_mod.split('\n')[0], 
                                                                    random.choice(mod_conquista),
                                                                    perdedor_mod.split('\n')[0], 
                                                                    len(dicc_descendente),
                                                                    tagganador,
                                                                    tagperdedor))

        tachar_barrio(perdedor)
        # print(tweet)
        api.update_with_media(imagen, tweet)
        pickle.dump( dicc_descendente, open( "./tmpdumps/dicc_descendente.p", "wb" ) ) # Actualiza el archivo dicc_descendente.p
        time.sleep(3)
        os._exit(0)
    
    if len(dicc_descendente) == 2: # Si quedan dos barrios, el tweet es del tipo:
        dos_barrios = set(dicc_descendente.keys())
        solo_uno = set([ganador])
        barrio_restante = dos_barrios-solo_uno
        tweet = ('{} {} {}. Ya solo quedan {} y {}!\n\n{} {}'.format(ganador_mod.split('\n')[0], 
                                                                        random.choice(mod_conquista),
                                                                        perdedor_mod.split('\n')[0], 
                                                                        ganador.split('\n')[0], 
                                                                        ''.join(barrio_restante).split('\n')[0],
                                                                        tagganador,
                                                                        tagperdedor))

        tachar_barrio(perdedor)
        # print(tweet)
        api.update_with_media(imagen, tweet)
        pickle.dump( dicc_descendente, open( "./tmpdumps/dicc_descendente.p", "wb" ) ) # Actualiza el archivo dicc_descendente.p
        time.sleep(3)
        os._exit(0)
        
    if len(dicc_descendente) == 1: # Cuando solo quede un barrio, el tweet es del tipo:
        tweet = ('{} {} {}, {} ha ganado la guerra. Toscano sigue siendo el alcalde...'.format(ganador_mod.split('\n')[0], 
                                                                                                           random.choice(mod_conquista),
                                                                                                           perdedor_mod.split('\n')[0], 
                                                                                                           ganador.split('\n')[0]))
        
        tachar_barrio(perdedor)
        # print(tweet)
        api.update_with_media(imagen, tweet)
        pickle.dump( dicc_descendente, open( "./tmpdumps/dicc_descendente.p", "wb" ) ) # Actualiza el archivo dicc_descendente.p
        time.sleep(3)
        os._exit(0)
