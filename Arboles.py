import os

class node():
    def __init__(self, dato):
        self.left = None
        self.right = None
        self.dato = dato

class arbol():
    def __init__(self):
        self.root = None
        
    def insert(self, a, dato):
        if a == None:
            a = node(dato)
        elif a != dato:
            d = a.dato
            if dato < d:
                a.left = self.insert(a.left, dato)
            elif dato > d:
                a.right = self.insert(a.right, dato)
        return a

    def inorder(self, a):
        if a == None:
            return None
        else:
            self.inorder(a.left)
            print(a.dato)
            self.inorder(a.right)

    def preorder(self, a):
        if a == None:
            return None
        else:
            print(a.dato)
            self.preorder(a.left)
            self.preorder(a.right)

    def postorder(self, a):
        if a == None:
            return None
        else:
            self.postorder(a.left)
            self.postorder(a.right)
            print(a.dato)

    def buscar(self, dato, a):
        if a == None:
            return None
        else:
            if dato == a.dato:
                return a.dato
            else:
                if dato < a.dato:
                    return self.buscar(dato, a.left)
                else:
                    return self.buscar(dato, a.right)

    def acceder(self, dato, a):
        if a == None:
            return None
        else:
            if dato == a.dato:
                return a
            else:
                if dato < a.dato:
                    return self.acceder(dato, a.left)
                else:
                    return self.acceder(dato, a.right)

    def insertar_rama_der(self, a, raiz):
        temp_izq = raiz.left
        raiz.right = a.right
        raiz.left = a.left
        i = raiz.left
        while i.left != None:
            i = i.left
        i.left = temp_izq

    def insertar_rama_izq(self, a, raiz):
        temp_der = raiz.right
        raiz.left = a.left
        raiz.right = a.right
        i = raiz.right
        while i.right != None:
            i = i.right
        i.right = temp_der


    
    def borrar(self, a, raiz):
        if  raiz.left.dato == a:
            insertar_rama_izq(a, raiz.left)  
        elif raiz.right.dato == a:
            insertar_rama_der(a, raiz.right)
        else:
            if a < raiz.dato:
                return self.borrar(a, raiz.left)
            else:
                return self.borrar(a, raiz.right)
            
                

tree = arbol()

while True:
    os.system("cls")
    print("Arbol ABB")
    opc = input("\n1.-Insertar nodo \n2.-Inorden \n3.-Preorden \n4.-Postorden \n5.-Buscar \n6.-Eliminar un nodo \n7.-Acceder a un nodo \n8.-Salir \n\nElige una opcion -> ")

    if opc == '1':
        nodo = input("\nIngresa el nodo -> ")
        if nodo.isdigit():
            nodo = int(nodo)
            tree.root = tree.insert(tree.root, nodo)
        else:
            print("\nIngresa solo digitos...")
    elif opc == '2':
        if tree.root == None:
            print("Vacio")
        else:
            tree.inorder(tree.root)
    elif opc == '3':
        if tree.root == None:
            print("Vacio")
        else:
            tree.preorder(tree.root)
    elif opc == '4':
        if tree.root == None:
            print("Vacio")
        else:
            tree.postorder(tree.root)
    elif opc == '5':
        nodo = input("\nIngresa el nodo a buscar -> ")
        if nodo.isdigit():
            nodo = int(nodo)
            if tree.buscar(nodo, tree.root) == None:
                print("\nNodo no encontrado...")
            else:
                print("\nNodo encontrado -> ",tree.buscar(nodo, tree.root), " si existe...")
        else:
            print("\nIngresa solo digitos...")   
    elif opc == '6':
        nodo = input("\nIngresa el nodo para eliminar -> ")
        if nodo.isdigit():
            nodo = int(nodo)
            if tree.buscar(nodo, tree.root) == None:
                print("\nNodo no encontrado...")
            else:
                print("\nÁrbol antes de ser eliminado el nodo %d en in-orden: " %(nodo))
                tree.inorder(tree.root)
                tree.borrar(nodo, tree.root)
                print("\nÁrbol después de eliminar el nodo %d en in-orden" %(nodo))
                tree.inorder(tree.root)
        else:
            print("\nIngresa solo digitos...")     
    elif opc == '8':
        print("\nElegiste salir...\n")
        os.system("pause")
        break
    else:
        print("\nElige una opcion correcta...")
    print()
    os.system("pause")

print()
