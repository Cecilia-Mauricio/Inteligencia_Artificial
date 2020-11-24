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
 
def profundidad(raiz,num):
    recorrido.append(raiz)
    if raiz == num:
        return num
    for a,b in Arbol.items():
        if b == raiz:
            r = profundidad(a,num)
            if r:
                return r
    recorrido.pop()
r = profundidad("10","30")

if r:
    print("Busqueda Exitosa")
    print("Se Muestra el Recorrido")
else:
    print("No Encontrado :(")

print(recorrido)