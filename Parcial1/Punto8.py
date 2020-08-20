#Punto número 8, Juan Felipe Martínez Bedoya

ti = input("Ingrese su número de identidad: ")

def imprimir_TI(s):
    num = int(s[len(s)-2]+s[len(s)-1])
    imprimir(num)

def imprimir(n):
    if(n == 1):
        print("1",end = "")
    else: 
        print("%s " %(n),end = "")
        imprimir(n-1)

print("Número de identidad: ",ti)
imprimir_TI(ti)
