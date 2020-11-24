#############################################
#          Garcia Sabino Montserrat         #
#           Mauricio Trejo Cecilia          #
#           Inteligencia Artificial         #
#############################################

import json
Arbol = False

with open ("Arbol.json","r") as read_file:
    data = json.load(read_file)
    Arbol = data['Arbol']

recorrido = []
camino = []
 
def anchura(raiz,num,iteraciones):
    recorrido.append(raiz)
    if raiz == num:
        return (True,iteraciones)
    buscar(raiz)
    if len(camino) == 0:
        return (False,iteraciones)
    return anchura(camino.pop(0),num,iteraciones+1)

def buscar(raiz):
    for a,b in Arbol.items():
        if b == raiz:
            camino.append(a)
 
r,iteraciones = anchura("10","30",1)

if r:
    print("Busqueda Exitosa")
    print("Se Muestra el Recorrido")
else:
    print("No Encontrado :(")
    
print(recorrido)