# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 18:57:42 2020

@author: garci
"""

#############################################
#          Garcia Sabino Montserrat         #
#           Mauricio Trejo Cecilia          #
#           Inteligencia Artificial         #
#############################################

#Ejercicio de clase

Def = [
        ("tortuga","garras"),
        ("tortuga","Proteccion queratina"),
        ("gallo","garras"),
        ("gallo","Proteccion queratina"),
        ("cocodrilo","garras"),
        ("cocodrilo","Proteccion queratina"),
        ("iguana","garras"),
        ("iguana","Proteccion queratina"),
        ("gato","g. mamarias"),
        ("gato","pelo"),
        ("gato","garras"),
        ("ballena","g. mamarias"),
        ("ballena","pelo"),
        ("oso","g. mamarias"),
        ("oso","pelo"),
        ("oso","garras"),
        ("delfin","g. mamarias")
        ]
Viv = [
        ("tortuga","agua"),
        ("gallo","tierra"),
        ("cocodrilo","agua"),
        ("iguana","tierra"),
        ("gato","tierra"),
        ("ballena","agua"),
        ("oso","tierra"),
        ("delfin","agua")
       ]

Ser = [
        ("tortuga","sauropsida"),
        ("gallo","sauropsida"),
        ("cocodrilo","sauropsida"),
        ("iguana","sauropsida"),
        ("gato","mammalia"),
        ("ballena","mammalia"),
        ("oso","mammalia"),
        ("delfin","mammalia"),
        ("mammalia","viviparo"),
        ("viviparo","tetrapodo"),
        ("sauropsida","oviparo"),
        ("oviparo","tetrapodo"),
        ("tetrapodo","vertebrado")
       ]



def Tiene(A,B,De):
    if not De:
        return False
    c = 0
    f = len(De)
    while c < f:
        if De[c][0] == A and De[c][1] == B:
            return True
        c = c + 1
    else:
        return False

def Vive(A,B,Vi):
    if not Vi:
        return False
    c = 0
    f = len(Vi)
    while c < f:
        if Vi[c][0] == A and Vi[c][1] == B:
            return True
        c = c + 1
    else:
        return False
                        
def Es(A,B,Se):
    if not Se:
        return False
    c = 0
    f = len(Se)
    while c < f:
        if Se[c][0] == A:
            if Se[c][1] == B:
                return True
            else:
                A = Se[c][1]
                c = -1
        c = c + 1
    else:
        return False
  
print (Tiene("araña","pelo",Def))
print (Vive("gallo","agua",Viv))
print (Es("mammalia","oviparo",Ser))
print (Tiene("gato","garras",Def))
print (Vive("tortuga","agua",Viv))
print (Es("mammalia","tetrapodo",Ser))

###########################################################################
#Funciona solo si el proceso es igual para cada comparacion 
###########################################################################
def esta(A,B,Vi):
    if not Vi:
        return False
    c = 0
    f = len(Vi)
    while c < f:
        if Vi[c][0] == A and Vi[c][1] == B:
            return True
        c = c + 1
    else:
        return False
def dato1(A):
    def dato2(B):
        def lista(Vi):
            return esta(A,B,Vi)
        return lista
    return dato2
############################################
#          wrappers
###########################################

def Tiene():
    return dato1("araña")("pelo")(Def)
print(Tiene())
def Vive():
    return dato1("gallo")("agua")(Viv)
print(Vive())
def Es():
    return dato1("mammalia")("oviparo")(Ser)
print(Es())
def Tiene():
    return dato1("gato")("garras")(Def)
print(Tiene())
def Vive():
    return dato1("tortuga")("agua")(Viv)
print(Vive())
def Es():
    return dato1("oviparo")("tetrapodo")(Ser)
print(Es())