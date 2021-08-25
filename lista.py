from nodo import nodo
class lista: 
    def __init__(self):
        self.cabeza = None
    def agregar_enfrente(self, info):
        self.cabeza = nodo(info=info, siguiente=self.cabeza)
    def vacio(self):
        return self.cabeza == None
    def agregaral_final(self, info):
        if not self.cabeza:
            self.cabeza = nodo(info=info)
            return
        reciente = self.cabeza
        while reciente.siguiente:
            reciente = reciente.siguiente
        reciente.siguiente = nodo(info=info)
    def mostrar_lista(self):
        nodo = self.cabeza
        while nodo != None:
            print(nodo.info, end =" => ")
            nodo = nodo.siguiente
        #entry = lista() # llamo a la lista a ser ejecutada
        #entry.agregar_enfrente(5) 
        #entry.agregaral_final(8) 
        #entry.agregar_enfrente(9) 
        #entry.mostrar_lista() 