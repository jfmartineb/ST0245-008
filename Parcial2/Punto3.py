def obtenerPostorden(preorden, inorden, postorden = []):
    izq = inorden[:inorden.index(preorden[0])]
    der = inorden[inorden.index(preorden[0])+1:]

    if len(izq) > 0:
        postorden = obtenerPostorden(preorden[1:], izq, postorden)

    if len(der) > 0:
        postorden = obtenerPostorden(preorden[len(izq)+1:], der, postorden)

    postorden.append(preorden[0])
    return postorden

inorden = ['I','A','B','E','G','L','D','C','F','M','K','H','J']
preorden = ['G','E','A','I','B','M','C','L','D','F','K','J','H']

print("Recorrido en postorden: ", obtenerPostorden(preorden, inorden))
