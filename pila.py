from nodo import Nodo
from graphviz import Digraph

class Pila(object):
    def __init__(self):
        self.cabeza = None
        self.cola = None
        self.size = 0
        self.contador = 0

    def insertar(self, terreno):
        nuevo = Nodo(terreno)
        
        if self.cabeza is None:
            self.cabeza = nuevo
            self.cola = self.cabeza
        else:
            self.cola.siguiente = nuevo
            self.cola = nuevo
        self.contador += 1

    def iterar(self):
        
        actual = self.cabeza

        while actual:
            dato = actual.dato
            actual = actual.siguiente
            yield dato

    def graficarMiLista(self):
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
    
    def imprimir(self):        
        for d in Pila.iterar:
            print(d)
    