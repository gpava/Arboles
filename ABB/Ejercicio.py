def llegada(arbol, nodollegada):

    if(nodollegada%2==0):
        return("El valor de llegada es el original: "+str(nodollegada))
    else:
        hermano = buscarNodo(arbol.raiz,nodollegada)
        if(hermano!=None and hermano%2==0):
         return("El valor de llegada es el hermano : "+str(hermano))
        else:
            return ("Esta muerto")


def buscarNodo(nodoActual, nodollegada):
    if(nodoActual.getIzquierda().getDato()==nodollegada):
        return nodoActual.getDerecha().getDato()
    elif (nodoActual.getDerecha().getDato() == nodollegada):
        return nodoActual.getIzquierda().getDato()
    else:
        buscarNodo(nodoActual.getIzquierda(),nodollegada)
        buscarNodo(nodoActual.getDerecha(), nodollegada)

    return