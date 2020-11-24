#############################################
#          Garcia Sabino Montserrat         #
#           Mauricio Trejo Cecilia          #
#           Inteligencia Artificial         #
#############################################

import json
Arbol = False

with open('ArbolCol.json','r') as info:
    data = json.load(info)
    Arbol = data["ArbolCol"]

def recorrido(camino):
    valorAnterior = 0
    valorMenor = 0
    L = []
    for i in camino:
        if valorAnterior == 0:
            L.append(i)
            valorAnterior = i[2]
        else:
            if i[2] <= valorAnterior:
                valorMenor = i[2]
                valorAnterior = i[2]
                L = []
                L.append(i)
            else:
                valorMenor = valorAnterior
                valorAnterior = i[2]
    return L

def subirColina():
    listaRetorno = []
    camino = []
    valor = str(input('Ingresa Un Valor Entre A y M: ')).upper()
    if valor == "":
        return "No es válido"
    if valor == Arbol[0][0]:
        return valor,"Es La Raíz"
    Elemento = [ e for e in Arbol if e[1] == valor]
    listaRetorno.append(Elemento[0])
    while Elemento[0][0] != Arbol[0][0]:
        Elemento = [ e for e in Arbol if e[1] == Elemento[0][0]]
        if len(Elemento) > 1:
            Elemento = recorrido(Elemento)
            listaRetorno.append(Elemento[0])
        else:
            listaRetorno.append(Elemento[0])
    return listaRetorno

A = subirColina()
if type(A) == list:
    A = A[::-1]
print("Busqueda Exitosa")
print("Se Muestra el Camino a Seguir ",A)