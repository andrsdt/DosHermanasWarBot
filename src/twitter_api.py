# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 16:58:43 2020

@author: andres
"""

import tweepy
import os

# Las creedenciales están almacenadas como variables de entorno, el usuario puede añadir las suyas
# en su sistema o sustituir directamente en la función por las que proporciona la API de Twitter
# Puede ser necesario cambiar la estructura de la función para tomar las variables de entorno desde
# Heroku o similares. Como está aquí escrito sólo está probado en Windows.

auth = tweepy.OAuthHandler(os.environ.get('CONSUMER_KEY'),os.environ.get('CONSUMER_SECRET'))
auth.set_access_token(os.environ.get('ACCESS_KEY'),os.environ.get('ACCESS_SECRET'))

api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication OK")
    
except:
    print("Error during authentication")
    
