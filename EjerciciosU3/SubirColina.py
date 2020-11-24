#############################################
#          Garcia Sabino Montserrat         #
#           Mauricio Trejo Cecilia          #
#           Inteligencia Artificial         #
#############################################

import json
import random
from operator import itemgetter
#para abrir nuestro documento json
with open('Arbol.json') as file:
	Conocimiento = json.load(file)


ruta=[]
way=[]
otra = []

def subida(inicial,objetivo,ant):
	ruta.append(inicial)
	print("La ruta actual es "+inicial)
	print("La ruta anterior fue "+ant)
	if otra:
		del otra[:]
		del way[:]
	if objetivo == inicial:
		print("Valor ha sido encontrado en ")
		return inicial
	if ant == "":
		ant = inicial
	for d in Conocimiento:
		if d[0] == inicial:
			if ant != "":
				if d[1] != ant:
					way.append(d)
	print(min(way, key=itemgetter(2))[:])
	print (way)
	Nuev = (min(way, key=itemgetter(2))[2])
	
	for c in way:
		if c[2] == Nuev:
			print("Entra")
			otra.append(c)
	print("Valores definitivos")
	print(otra)
	cont = 0
	for n in otra:
		cont = cont +1
		if cont > 1:
			r = random.random()
			print("n")
			print(n)
			if r < 0.5:
				otra.pop()
			else: 
				otra.pop(0)
		else:
			print(otra)
	if otra:
		for n in otra:
			print("Nodo")
			print(n[1])
			return subida(n[1],objetivo,inicial)


arch=subida("A","H","")
if arch:
	print("Nodo")
	print(arch)
	print("Ruta")
	print(ruta)