#############################################
#          Garcia Sabino Montserrat         #
#           Mauricio Trejo Cecilia          #
#           Inteligencia Artificial         #
#############################################

import json


with open ("Arbol2.json","r") as read_file:
	data = json.load(read_file)
	Grafo = data['Arboles']

def nodos(valor):
	i = 0
	nodo = []
	lista = []
	for e in Grafo:
		lista = lista+[e["rama"].split()]
		nodo = nodo+[e["nodo"].split()]
	for e in lista:
		print (nodo[i],lista[i][0])
		if (lista[i][0] == valor):
			return True
		i += 1

R = nodos("16")
if(R == True):
	print ("Raiz")