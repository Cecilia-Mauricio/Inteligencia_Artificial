# -*- coding: utf-8 -*-
"""
Created on Mon Oct  25 18:37:36 2020

@author: garci
"""
#############################################
#          Garcia Sabino Montserrat         #
#           Mauricio Trejo Cecilia          #
#           Inteligencia Artificial         #
#############################################

basura = [
        "Los","de","Cual","fue","Ya","casi","Que","te","si","a","un","de","todo","no","con"
        ]

import json
strem = False
i = 0

with open("tweet.json","r") as read_file:
	data = json.load(read_file)
	strem = data['Tweets']

def compatibles(matriz):
	print()
	print("json compatible con el programa de clasificacion")
	i = 0
	data = {}
	data["Probabilidades"] = []
	while i < len(matriz):
		data["Probabilidades"].append([matriz[i][0],matriz[i][4]])
		i = i + 1
	with open('base.json', 'w') as file:
		json.dump(data, file, indent=1)
	with open("base.json","r") as read_file:
		data = json.load(read_file)
		tw = data["Probabilidades"]
	return(tw)
    
def matriz(strem,p,nstrem):
	i = 0
	s = 0
	n = 0
	matr = []
	print("Matriz de probabilidades")
	while i < len(p):
		j = 0
		while j < len(strem):
			if strem[j] == p[i]:
				s = s + 1
			n = nstrem - s
			j = j + 1
		t = s + n
		matr.append([p[i], n, s, t, s/t, n/t])
		s = 0
		n = 0
		i = i + 1
	print(matr)
	return compatibles(matr)

def advervios(tweet,basura):
	j = 0
	k = []
	C = []
	while j < len(tweet):
		i = 0
		while i < len(tweet[j]):
			if not tweet[j][i] in basura:
				s = tweet[j][i]
				k = k + [s]
			i = i + 1
		j = j + 1
	j = 0
	while j < len(k):
		if not k[j] in C:
			C = C + [k[j]]
		j = j + 1 
	return matriz(k,C, len(tweet))


def separar(strem,basura,t = []):
	i = 0
	while i < len(strem):
		tw = strem[i]
		Stream = tw['Stream']
		texto = tw['texto']
		if Stream == True:
			texto = texto.split()
			t = t + [texto]
		i = i +1
	return advervios(t,basura)

print(separar(strem,basura))