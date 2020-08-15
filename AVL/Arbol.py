class Arbol():
    def _init_(self):
        self.Raiz=None

    def getRaiz(self):
        return self.Raiz

# obtener fe
    def obtenerFe(self,Padre):
        if Padre == None:
            return -1
        else:
            return Padre.getFe()

# rotacion simple izquierda, roto hacia la derecha
    def rotacionIzquierda(self,Padre):
        aux = Padre.getIzq()
        Padre.setIzq(aux.getDer())
        aux.setDer(Padre)
        #actualizo las alturas
        Padre.setFe(max(self.obtenerFe(Padre.getIzq()), self.obtenerFe(Padre.getDer())) + 1)
        aux.setFe(max(self.obtenerFe(aux.getIzq()), self.obtenerFe(aux.getDer())) + 1)
        return aux

# rotacion simple derecha, roto hacia a la izquierda
    def rotacionDerecha(self,Padre):
        aux = Padre.getDer()
        Padre.setDer(aux.getIzq())
        aux.setIzq(Padre)
        #actualizo alturas
        Padre.setFe(max(self.obtenerFe(Padre.getIzq()), self.obtenerFe(Padre.getDer())) + 1)
        aux.setFe(max(self.obtenerFe(aux.getIzq()), self.obtenerFe(aux.getDer())) + 1)
        return aux

# rotacion doble a la izquieda
    def rotacionDobleIzquierda(self,Padre):
         #Detecto que hay un desbalance por derecha para girar hacia la izquierda
        Padre.setIzq(self.rotacionDerecha(Padre.getIzq()))
        aux = self.rotacionIzquierda(Padre)
        return aux

# rotacion doble derecha
    def rotacionDobleDerecha(self,Padre):
          #Detecto que hay un desbalance por izquierda para girar hacia la derecha
        Padre.setDer(self.rotacionIzquierda(Padre.getDer()))
        aux = self.rotacionDerecha(Padre)
        return aux

    def insertar(self,Nuevo):
        if  self.Raiz == None:
            self.Raiz = Nuevo
        else:
            self.Raiz = self.insertarAvl(Nuevo, self.Raiz)

# metodo para ingresar datos
    def insertarAvl(self,Nuevo,subArbol):
        nuevoPadre = subArbol
        if Nuevo.getDato() < subArbol.getDato():
            if subArbol.getIzq() == None:
                 subArbol.setIzq(Nuevo) # ingreso a la izquierda
            else:
                subArbol.setIzq(self.insertarAvl(Nuevo, subArbol.getIzq()))
                if (self.obtenerFe(subArbol.getIzq()) - self.obtenerFe(subArbol.getDer())) == 2: # desbalanceo DFE
                    if Nuevo.getDato() < subArbol.getIzq().getDato():
                        nuevoPadre=self.rotacionIzquierda(subArbol)
                    else:
                        nuevoPadre=self.rotacionDobleIzquierda(subArbol)
        if Nuevo.getDato() > subArbol.getDato():
            if subArbol.getDer() == None:
                subArbol.setDer(Nuevo)
            else:
                subArbol.setDer(self.insertarAvl(Nuevo, subArbol.getDer()))
                if (self.obtenerFe(subArbol.getDer()) - self.obtenerFe(subArbol.getIzq())) == 2:
                    if Nuevo.getDato() > subArbol.getDer().getDato():
                        nuevoPadre = self.rotacionDerecha(subArbol)
                    else:
                        nuevoPadre = self.rotacionDobleDerecha(subArbol)
        # Actualizando Alturas
        self.ActualizarFe(subArbol)
        return nuevoPadre


    def ActualizarFe(self,Padre):
        if Padre.getIzq() == None and Padre.getDer() != None:
            Padre.setFe(Padre.getDer().getFe() + 1)
        if Padre.getIzq() != None and Padre.getDer() == None:
            Padre.setFe(Padre.getIzq().getFe() + 1)
        if Padre.getIzq() != None and Padre.getDer() != None:
            Padre.setFe(max(self.obtenerFe(Padre.getIzq()), self.obtenerFe(Padre.getDer())) + 1)
        if Padre.getIzq() == None and Padre.getDer() == None:
            Padre.setFe(1)

    def Recorrido(self,Padre):
        if Padre == None:
            return
        self.Recorrido(Padre.getIzq())
        print("",format(Padre.getDato()))
        self.Recorrido(Padre.getDer())