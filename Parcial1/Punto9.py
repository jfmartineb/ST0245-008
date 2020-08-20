#Punto número 9, Juan Felipe Martínez Bedoya

i = int(input("Ingrese cuantas filas del triangulo desea imprimir: "))

def  pascal(row, column):
    if row < 0 and column < 0:
        return 0
    elif row == 0 and column == 0:
        print("1")
    else: 
        if column < 0:
            pascal(row-1,row-1)
            
        else:
            if column == row:
                pascal(row,column-1)
                print("%d " %(combinacion(row,column)))
            else: 
                pascal(row,column-1)
                print("%d " %(combinacion(row,column)),end = "")

def combinacion(n,k):
    return int((factorial(n))/(factorial(k)*(factorial(n-k))))

def factorial(n):
    if (n == 0):
        return 1
    else:
        return n * factorial(n-1)

pascal(i,i)
