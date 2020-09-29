import time

#Punto 1

def repetidos1(lista):
    lista2 = []
    for i in lista:
        if(i not in lista2):
            lista2.append(i)

    return lista2

#Punto 2

def repetidos2(lista):
    lista2 = []
    for i in range(len(lista)-1):
        if lista[i-1] != lista[i]:
            lista2.append(lista[i])   

    return lista2

#Efectividad por tiempo punto 1 y 2

lista_p = [2,2,3,4,5,6,6,7,7,7,8,9,10,11,11]
tiempo1 = 0
tiempo2 = 0
for j in range(0,1000):
    t = time.time()
    repetidos1(lista_p)
    tiempo1 = tiempo1 + (time.time()-t)

    t2 = time.time()
    repetidos2(lista_p)
    tiempo2 = tiempo2 + (time.time() - t2)

prom1 = tiempo1/1000
prom2 = tiempo2/1000
print("La efectividad por tiempo del algoritmo repetidos 1 es: ",prom1)
print("La efectividad por tiempo del algoritmo repetidos 2 es: ",prom2)
print(prom1 > prom2)
#Punto 5

def votos(lista):
    lista1 = []
    votos = []
    for i in lista:
        if i not in lista1:
            lista1.append(i)
            votos.append(1)
        else:
            votos[lista1.index(i)] = votos[lista1.index(i)] + 1

    maxi = 0;
    for i in range(len(votos)-1):
        if votos[i] > votos[maxi]:
            maxi = i

    return lista1[maxi]

#Complejidad punto 5

lista_p = [2,2,2,2,2,3,3,3,3,4,4,5,5,5,5,6,2,2,4,5,6,2,3,2,2,2,2,2,2,3,4,3,5]
tiempo3 = 0
for j in range(0,1000):
    t = time.time()
    votos(lista_p)
    tiempo3 = tiempo3 + (time.time()-t)
prom3 = tiempo3/1000
print("\nLa efectividad por tiempo del algoritmo contador de votos es: ",prom3)

#Punto 7

def negativos(lista):
    lista_n = []
    for i in lista:
        if i < 0:
            lista_n.append(i)

    return lista_n

#Efectividad punto 7

lista_p = [-1,-1,-1,-1,-1,-1,-5,-6,-8,-8]
tiempo4 = 0
for j in range(0,1000):
    t = time.time()
    negativos(lista_p)
    tiempo4 = tiempo4 + (time.time()-t)
prom4 = tiempo4/1000
print("\nLa efectividad por tiempo del algoritmo buscador de negativos en el peor caso es: ",prom4)

#Punto 10

def busq_matriz(lista, elem):
    for i in lista:
        for j in i:
            if j == elem:
                return "Sí"
            elif j > elem:
                break
            
    return "No"

#Punto 11

def quick_sort2(lista):
    izq = []
    der = []
    centro = [] #sublista de un elemento

    if len(lista) > 1:
        pivote = lista[len(lista)-1] #con el último elemento en vez del primero
        for i in lista:
            if i < pivote: 
                izq.append(i)
            elif i == pivote:
                centro.append(i)
            else:
                der.append(i)
            
        return quick_sort(izq) + centro + quick_sort(der)


#pruebas
lista1 = [4,7,11,4,9,5,11,7,3,5]
print("\nPunto 1:")
print("Antes de identificar repetidos: ",lista1)
print("Después de indentifica repetidos: ",repetidos1(lista1))

lista2 = [2,2,3,4,5,5,5,6,7,8,9]
print("\nPunto 2: ")
print("Antes de identificar repetidos: ",lista2)
print("Después de indentifica repetidos: ",repetidos2(lista2))

candidatos = [2,2,2,2,2,3,3,3,3,4,4,5,5,5,5,6,2,2,4,5,6,2,3]
print("\nPunto 5:")
print("Basandose en los siguientes votos: ",candidatos)
print("El ganador es: ",votos(candidatos))

print("\nPunto 6:")
futbolistasTup = [(1, "Casillas"), (15, "Ramos"), (3, "Pique"), (5, "Puyol"), (11, "Capdevila"),
                  (14, "Xabi Alonso"), (16, "Busquets"), (8, "Xavi Hernandez"), (18, "Pedrito"), 
                  (6, "Iniesta"), (7, "Villa")]
print("Tupla antes del sort: ",futbolistasTup)
futbolistasTup.sort()
print("Tupla después del sort(): ",futbolistasTup)

futbolistasTup = [(1, "Casillas"), (15, "Ramos"), (3, "Pique"), (5, "Puyol"), (11, "Capdevila"),
                  (14, "Xabi Alonso"), (16, "Busquets"), (8, "Xavi Hernandez"), (18, "Pedrito"), 
                  (6, "Iniesta"), (7, "Villa")]
print("Tupla antes del sort: ",futbolistasTup)
futbolistasTup.sort(key=lambda futbolista : futbolista[1])
print("Tupla después del sort(key=lambda futbolista: futbolista[0]): ",futbolistasTup)

lista_n = [2,2,2,8,4,-4,5,6-5,-6,-8,-9,7,5,-9]
print("\nPunto 7: ")
print("Basandose en la siguiente lista : ",lista_n)
print("Se tienen lo siguientes número negativos: ",negativos(lista_n))

matrix = [[1,2,3,4],[1,3,3,5],[2,3,4,5],[3,4,4,6]]
print("\nPunto 10: ")
print("Matriz a analizar: ",matrix)
print("El elemento 6 %s está en la matriz" %(busq_matriz(matrix,6)))
