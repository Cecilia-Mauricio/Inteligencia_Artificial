#############################################
#          Garcia Sabino Montserrat         #
#           Mauricio Trejo Cecilia          #
#           Inteligencia Artificial         #
#############################################


tab =[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
plase = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
nqueen = 4
posi =[]
llave = 0
def cuaqueen(nqueen, tab, llave, plase):
    nueva = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    m = 0
    print("numero de reinas: "+str(nqueen))
    if nqueen == 1:
        return resp(tab)
    else: 
        for i in range(len(tab)):
            for j in range(len(tab[i])):
                if m == 0:
                  if plase[i][j] != 3:
                        if(tab[i][j] == 0):
                            if nqueen == 4:
                                plase[i][j] = 3
                            tab[i][j] = 1
                            m = m + 1
                            posi.append([i,j])
        tab = vec(tab,posi)
        posi.pop(0)
        for i in tab:
            if 0 in i:
               llave = 0
            else:
               llave = 1
        if llave == 1:
            print(llave)
            for i in nueva:
                print(i)
            nqueen=4
            llave=0
            return cuaqueen(nqueen,nueva,llave,plase)
        if llave == 0:
            print(llave)
            nqueen=nqueen-1
            return cuaqueen(nqueen,tab,llave,plase)

def vec(tab,posi):
    print("recorre")
    a = posi[0][0]
    b = posi[0][1]
    j = range(len(tab))
    d = b
    c = a
    print(posi)
    
    for i in range(len(tab)):
        for j in range(len(tab[i])):
            tab[a][j] = 2
            tab[i][b] = 2
    imprimir(tab)
    for t in range(len(tab)):
        d = d - 1
        c = c - 1
        if (d >= 0)and(c >=0):
            print("- -")
            tab[c][d] = 2
    d = b
    c = a
    imprimir(tab)
    for t in range(len(tab)):
        c = c + 1
        d = d + 1
        if (c <= j)and(d <= j):
            print("+ +")
            tab[c][d] = 2

    d = b
    c = a
    imprimir(tab)
    for i in range(len(tab)):
        d = d+1
        c = c -1
        if (d < j)and(c >=0):
            print("+ -")
            tab[c][d] = 2
    d = b
    c = a
    imprimir(tab)
    for t in range(len(tab)):
        d = d-1
        c = c + 1
        if (d >= 0)and(c <j):
            print("- +")
            tab[c][d] = 2
    tab[a][b]= 1
    imprimir(tab)
    print("termina de posicionar")
    return tab
   
def resp(tab):
    for i in range(len(tab)):
        for j in range(len(tab[i])):
            if (tab[i][j]) == 0:
                tab[i][j] = 1
    print("tablero final")
    for i in tab:
        print(i)

def imprimir(tab):
   print("")
   for i in tab:
       print(i)

cuaqueen(nqueen,tab,llave,plase)