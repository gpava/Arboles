from Arboles.ABB.Node import *
class Arbol:
    def __init__(self):
        self._root = None

    def addNode(self, label, value):
        if (self._root):
            self._addNode(label, value, self._root)
        else:
            self._root = Node(label, value)

    def _addNode(self, label, value, parent):
        if (value > parent.getValue()):
            rc = parent.hasRightChild()
            if(rc):
                self._addNode(label,value,rc)
            else:
                newNode = Node(label,value,parent)
                parent.setRightChild(newNode)
        elif(value < parent.getValue()):
            lc = parent.hasLeftChild()
            if (lc):
                self._addNode(label, value, lc)
            else:
                newNode = Node(label, value, parent)
                parent.setLeftChild(newNode)
        else:
            print("Este Nodo con el valor", value, "ya existe")

    def searchNode(self,label):
        if(self._root):
            return self._searchNode(label, self._root)
        else:
            print("el arbol está vacío")

    def _searchNode(self,label,parent):
        if(not parent):
            return None
        if(label==parent.getLabel()):
            return parent
        else:
            node = self._searchNode(label,parent.hasLeftChild())
            if(not node):
                node = self._searchNode(label,parent.hasRightChild())
            return node

    def inorder(self):
        if(self._root):
            self._inorder(self._root)
        else:
            print("Arbol vacío")

    def _inorder(self, parent):
        if(parent):
            self._inorder(parent.hasLeftChild())
            print(parent.getValue())
            self._inorder(parent.hasRightChild())

    def preorder(self):
        if (self._root):
            self._preorder(self._root)
        else:
            print("Arbol vacío")

    def _preorder(self, parent):
        if (parent):
            print(parent.getValue())
            self._preorder(parent.hasLeftChild())
            self._preorder(parent.hasRightChild())

    def postorder(self):
        if (self._root):
            self._postorder(self._root)
        else:
            print("Arbol vacío")

    def _postorder(self, parent):
        if (parent):
            self._postorder(parent.hasLeftChild())
            self._postorder(parent.hasRightChild())
            print(parent.getValue())

    def inorderList(self):
        if (self._root):
            nl = []
            self._inorderList(self._root,nl)
            print(nl)
        else:
            print("Arbol vacío")

    def _inorderList(self, parent, nodeList):
        if (parent):
            self._inorderList(parent.hasLeftChild(), nodeList)
            nodeList.append(parent.getValue())
            self._inorderList(parent.hasRightChild(), nodeList)

    def postorderList(self):
        if (self._root):
            nl = []
            self._postorderList(self._root,nl)
            print(nl)
        else:
            print("Arbol vacío")

    def _postorderList(self, parent, nodeList):
        if (parent):
            self._postorderList(parent.hasLeftChild(), nodeList)
            self._postorderList(parent.hasRightChild(), nodeList)
            nodeList.append(parent.getValue())


    def preorderList(self):
        if (self._root):
            nl = []
            self._preorderList(self._root,nl)
            print(nl)
        else:
            print("Arbol vacío")

    def _preorderList(self, parent, nodeList):
        if (parent):
            nodeList.append(parent.getValue())
            self._preorderList(parent.hasLeftChild(), nodeList)
            self._preorderList(parent.hasRightChild(), nodeList)

    def removeNode(self, label):
        if(self._root):
            targetNode= self.searchNode(label)
            if(targetNode):
                self._removeNode(targetNode)
                print("Nodo eliminado")
            else:
                print("elemento con", label, "no existe")
        else:
            print("arbol vacío")

    def _removeNode(self, node):
        if(node.isLeaf()):#Nodo hoja
            if(node.isLeftChild()):
                node.getParent().setLeftChild(None)
                node.setParent(None)
            else:
                node.getParent().setRightChild(None)
            node.setParent(None)
        else:
            #Nodo con dos hijos
            if(node.hasLeftChild() and node.hasRightChild()):
                suc = self._getSucessor(node.hasRightChild())
                self._updateNode(node, suc)
                if(suc.isLeaf()):
                    suc.getParent().setLeftChild(None)
                    suc.setParent(None)
                else:
                    suc.getParent().setLeftChild(suc.hasRightChild())
                    suc.hasRightChild().setParent(suc.getParent())
                    suc.setRightChild(None)
                    suc.setParent(None)
            else: #Nodo tiene un solo hijo
                if(node.isLeftChild()):
                    if(node.hasLeftChild()):
                        node.getParent().setLeftChild(node.hasLeftChild())
                        node.hasLeftChild().setParent(node.getParent())
                        node.setLeftChild(None)
                    else:
                        node.getParent().setLeftChild(node.hasRightChild())
                        node.hasRightChild().setParent(node.getParent())
                        node.setRightChild(None)
                else:
                    if(node.hasLeftChild()):
                        node.getParent().setRightChild(node.hasLeftChild())
                        node.hasLeftChild().setParent(node.getParent())
                        node.setLeftChild(None)
                    else:
                        node.getParent().setRightChild(node.hasRightChild())
                        node.hasRightChild().setParent(node.getParent())
                        node.setRightChild(None)
                node.setParent(None)

    def _getSucessor(self, node):
        lc = node.hasLeftChild()
        if(lc):
            return self._getSucessor(lc)
        else:
            return node

    def _updateNode(self, oldNode, newNode):
        oldNode.setValue(newNode.getValue())
        newNode.setLabel(newNode.getLabel())


