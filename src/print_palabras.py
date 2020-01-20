# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 17:42:19 2020

@author: andres
"""

from PIL import Image, ImageFont, ImageDraw
from sort_barrios import leer_archivo

barrios = leer_archivo('./data/barrios_ordenados.txt')
font = ImageFont.truetype('./data/fonts/Roboto-Light.ttf', size=40, encoding="unic")
image = Image.open('./data/background/actual.png')
draw = ImageDraw.Draw(image)


def imprimir_texto(barrios): # Guarda una imagen con todos los barrios sin tachar, y de vuelve un diccionario de la forma [(Costa del Sol, (100,100)), (Cerro Blanco, (100,175)...]
    image = Image.open('./data/background/actual.png')
    draw = ImageDraw.Draw(image)

    coordenadas_barrio = {}
    
    x = 100 
    y = 100 # Coordenadas iniciales para escribir el primer barrio en la imagen
    
    for b in barrios:
        draw.text((x, y),b, fill='black', font=font) # Escribe todos los barrios en la imagen
        if b not in coordenadas_barrio:
            coordenadas_barrio[b] = (x,y) # Va añadiéndolos al diccionario coordenadas_barrio con sus respectivas coordenadas para usarlo después

        if y >= image.size[1]-200:
            x += 465
            y = 100
        else:
            y += 75
            
            # Si la distancia entre la palabra y el borde inferior es menor a 200, suma 465 a la coordenada horizontal y establece la vertical en 100.
            # Dicho de otra forma, iniciar una nueva columna
            
    image.save('./out/subir/updated_img.png', optimize = True) # Guarda la imagen como updated_img.png, que más tarde usaremos para tachar
    
    return list(coordenadas_barrio.items()) # Devuelve una lista de la forma [(Costa del Sol, (100,100)), (Cerro Blanco, (100,175)...)]

def tachar_todo(barrios): # Tacha todos los barrios. Función de prueba, después no se usa
    image = Image.open('./out/imprimir_texto.png')
    draw = ImageDraw.Draw(image)
    
    for entrada in imprimir_texto(barrios):
        
        xi = entrada[1][0]-10 
        xf = xi + font.getsize(entrada[0])[0]
        yi = entrada[1][1]+25
        yf = yi
        
        draw.line([(xi,yi), (xf,yf)], fill='red', width = 5)
    
    image.save('./out/tachar_todo.png', optimize = True)


def tachar_barrio(perdedor, foto ='./out/subir/updated_img.png'): # Genera una imagen con el barrio introducido como parámetro tachado
    image = Image.open(foto)
    draw = ImageDraw.Draw(image)
    
    for entrada in imprimir_texto(barrios):
        if entrada[0] == perdedor or entrada[0] == perdedor+'\n': # Los barrios tienen \n al final asi que lo añado al que yo le meto como parámetro
            
            # entrada es del tipo (Costa del Sol, (100,100)) 
            x = entrada[1][0] # Coordenada x
            y = entrada[1][1] # Coordenada y
            b = entrada[0]    # Nombre del barrio
            
            draw.text((x, y),b, fill='red', font=font, size=40, encoding="unic") # Escribir la palabra otra vez pero en rojo, con la misma fuente y el mismo tamaño para que tape la anterior
            
            # COORDENADAS DE LA LINEA DE TACHADO
            
            xi = entrada[1][0]-10 # Resto 10 en la coordenada horizontal inicial de la palabra para que la linea empiece un poco antes que la palabra
            xf = xi + font.getsize(entrada[0])[0] # Sumo la longitud en pixeles de la palabra, y esa es la coordenada x final
            yi = entrada[1][1]+25 # Sumo 25 para que la línea esté aproximadamente en el centro de la palabra
            yf = yi # Puesto que es una línea horizontal, la coordenada vertical no varía

            draw.line([(xi,yi), (xf,yf)], fill='red', width = 3) # Dibujo la línea de tachado con anchura 3 y en rojo

    image.save(foto, optimize = True) # Guardo la imagen como updated_img.png que a la vez es la que entra como parámetro por defecto


# ================== FUNCIONES DE PRUEBA ==================
    
# if __name__ == '__main__':
        # ordenar_barrios(barrios)
        # imprimir_texto(barrios)
        # tachar_todo(barrios)
        # tachar_barrio(perdedor)
        # tachar_barrio('Ibarburu')