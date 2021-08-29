from nodo import nodo
from graphviz import Digraph

class Pila:
    def __init__(self):
        self.ultimo = None
        self.size = 0

    def apilar(self, valor):
        nuevo = nodo(valor)
        if (self.size == 0):
            self.ultimo = nuevo
            nuevo.siguiente = None
            self.size = 1
        else:
            nuevo.siguiente = self.ultimo
            self.ultimo = nuevo
            self.size += 1

    def desapilar(self):
        if (self.size == 0):
            return 'Pila vacia...!!!'
        elif self.ultimo.siguiente == None:
            valor = self.ultimo.valor
            self.ultimo = None
            self.size = 0
            return valor
        else:
            valor = self.ultimo.valor
            aux = self.ultimo.siguiente
            self.ultimo.siguiente = None
            self.ultimo = aux
            self.size -= 1
            return valor

    def graficarPila(self):
        dot = Digraph(comment='Grafica de la pila...!!')
        aux = self.ultimo
        contador = 0
        while aux != None:
            contador += 1
            dot.node(str(contador), str(aux.valor))
            aux = aux.siguiente
            if(contador <= self.size and contador >1):
                dot.edge(str(contador-1), str(contador))
        dot.render("Pila", format="png", view=True)
    
    def imprimirPila(self):        
        aux = self.ultimo
        contador = 0
        while aux != None:
            contador += 1
            print(aux.valor)
            aux = aux.siguiente
            if (aux.siguiente == None):
                break
    