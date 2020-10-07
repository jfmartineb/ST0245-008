import pandas as pd
import numpy as np

file = pd.read_csv('TEST lite.csv', sep=';')

def separador(x):
    matriz = np.matrix(x.values)
    for i in range(len(matriz)):
        s = matriz[i, 18]
        s = s[-4:]
        p = matriz[i, 19]
        p = p // 10
        matriz[i, 18] = int(p) - int(s)
        if matriz[i, 1] == 'NO':
            matriz[i, 1] = 00
    matriz1 = np.delete(matriz, [0, 11, 12, 22, 24, 48, 50, 57, 58, 62, 64], 1)
    return matriz1

print(separador(file)[:, -1].transpose().tolist()[0])
print(separador(file)[:, :-1].tolist())
x = separador(file)[:, :-1].tolist()
y = separador(file)[:, -1].transpose().tolist()[0]
