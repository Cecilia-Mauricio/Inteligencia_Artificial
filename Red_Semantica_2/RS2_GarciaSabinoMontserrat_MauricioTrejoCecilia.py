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
Conocimiento = False

with open ("ani.json", "r") as read_file:
    data = json.load(read_file)
    Conocimiento = data['conocimiento']
    
    
    
def esta(A,B,C,CON):
    if not CON:
        return False
    c = 0
    f = len(CON)
    if B == "Vive" or B == "Tiene":
        while c < f:
            if CON[c][0] == A and CON[c][1] == B and CON[c][2] == C:
                return True
            c = c + 1
        else:
            return False
    else:
        while c < f:
            if CON[c][0] == A:
                if CON[c][1] == B:
                    if CON[c][2] == C:
                        return True
                    else:
                        A = CON[c][2]
                        c = -1
            c = c + 1
        else:
            return False

def consulta(A,B,C):
    return esta(A,B,C,Conocimiento)

def main():
    print("Bienvenido a este programa")
    print('Puedes consultatar escribiendo consulta("<Animal>","<Tiene>","<Caracteristica>")')
    print('Puedes consultatar escribiendo consulta("<Animal>","<Vive>","<agua/tierra>")')
    print('Puedes consultatar escribiendo consulta("<Animal/Clasificacion>","<es>","<Clasificacion>")')
    print("Para salir presiona 'q' o escribe quit()")
    Terminar= False
    while not Terminar:
        Leer = input("> ")
        if Leer == 'q':
            return
        Imprimir = eval(Leer)
        print(Imprimir)
        
if __name__ == "__main__":
     main()
    
