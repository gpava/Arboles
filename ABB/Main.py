from Arboles.ABB.Arbol import *

def Main():
   mytree = Arbol()
   mytree.addNode(36, 36)
   mytree.addNode(45, 45)
   mytree.addNode(22, 22)
   mytree.addNode(3, 3)
   mytree.addNode(58, 58)
   mytree.addNode(39, 39)
   mytree.addNode(28, 28)
   mytree.addNode(35, 35)
   mytree.addNode(7, 7)
   mytree.addNode(15, 15)
   mytree.addNode(13, 13)
   print("Recorrido Preorder")
   print("----------")
   mytree.preorder()
   print("Recorrido Inorder")
   print("---------")
   mytree.inorder()
   print("Recorrido Postorder")
   print("---------")
   mytree.postorder()
   print("--------")
   print("Recorrido Preorder en lista")
   print("----------")
   mytree.preorderList()
   print("Recorrido Inorder en lista")
   print("---------")
   mytree.inorderList()
   print("Recorrido Postorder en lista")
   print("---------")
   mytree.postorderList()
   print("--------")
   print("... buscando el 35")
   fn = mytree.searchNode(35)
   if (fn):
      print("label", fn.getLabel())
      print("valor", fn.getValue())
   else:
      print("No se encuentra en el arbol")
   print("... Eliminando el 35")
   mytree.removeNode(35)
   print("--------")
   mytree.preorder()
   print("... Eliminando el 7")
   mytree.removeNode(7)
   print("--------")
   mytree.preorder()
   print("... Eliminando el 15")
   mytree.removeNode(15)
   print("--------")
   mytree.preorder()
   print("... Eliminando el 13")
   mytree.removeNode(13)
   print("--------")
   mytree.preorder()
   print("... Eliminando el 3")
   mytree.removeNode(3)
   print("--------")
   mytree.preorder()
   print("... Eliminando el 28")
   mytree.removeNode(28)
   print("--------")
   mytree.preorder()
   print("... Eliminando el 36")
   mytree.removeNode(36)
   print("--------")
   mytree.preorder()
   print("... Eliminando el 39")
   mytree.removeNode(39)
   print("--------")
   mytree.preorder()

Main()