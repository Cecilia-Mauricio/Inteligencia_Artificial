# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 18:37:36 2020

@author: garci
"""
#############################################
#          Garcia Sabino Montserrat         #
#           Mauricio Trejo Cecilia          #
#           Inteligencia Artificial         #
#############################################
import json
from io import open
Conocimiento = False

with open("base.json", "r") as read_file:
    data = json.load(read_file)
    Conocimiento = data['Probabilidades']
#abre archivo 
archivo = open ('tweet.txt','r')
a = archivo.read()
t = a.split()
archivo.close()

def es_stream(tex, CON):
    suma = 0
    promedio = 0
    l = len(tex)
    l1 = len(CON)
    comparacion = []
    for i in range(l):
        for j in range (l1):
            if CON[j][0] == t[i]:
                comparacion.append(CON[j])
        for l in range(len(comparacion)):
            suma += float(comparacion[l][1])
            promedio = suma / len(comparacion)
        if (promedio > .55):
            return "Stream"
        else:
            return "No es stream"

print(es_stream(t, Conocimiento))

