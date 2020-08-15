class Nodo():
    def _init_(self, dato):
        self.dato = dato;
        self.fe=0;#altura del nodo
        self.Izq = None;
        self.Der = None;

    def getDato(self):
        return self.dato

    def getIzq(self):
        return self.Izq

    def getDer(self):
        return self.Der

    def setDato(self, dato):
        self.dato = dato;

    def setDer(self, Der):
        self.Der = Der

    def setIzq(self, Izq):
        self.Izq = Izq;

    def setFe(self,fe):
        self.fe=fe
    def getFe(self):
        return self.fe