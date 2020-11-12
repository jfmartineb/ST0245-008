class Pila:        
    def __init__(self):        
        self.items = [] 

    def no_vacia(self):        
        return len(self.items) == 0

    def inspeccionar(self):        
        assert not self.no_vacia()        
        return self.items[-1]        
        
    def apilar(self, elemento):        
        self.items.append(elemento)            
        
    def desapilar(self):        
        assert not self.no_vacia()        
        return self.items.pop()

    def peek(self):
        if len(self.items) > 0:
            return self.items[-1]
        else: 
            return None

    def __str__(self):
        return str(self.items)

def invertirPila(pila1, pila2):
    if not pila1.no_vacia():
        temp = pila1.desapilar()
        p2.apilar(temp)    
        invertirPila(pila1, pila2)
        
        


p1 = Pila()
p1.apilar(2)
p1.apilar(5)
p1.apilar(65)
p1.apilar(1)
p1.apilar(98)
p2 = Pila()

print("\nAntes de aplicar la función: ")
print("Pila 1: ",p1)
print("Pila 2: ",p2)



invertirPila(p1, p2)
print("\nDespués de aplicar la función: ")
print("Pila 1: ", p1)
print("Pila 2: ", p2)
