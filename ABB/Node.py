class Node:
    def __init__(self,label,value,parent = None):
        self._label=label
        self._value=value
        self._rightChild=None
        self._leftChild = None
        self._parent=parent

    def setValue(self, n):
        self._value = n

    def setLabel(self, l):
        self._label = l

    def getValue(self):
        return self._value

    def hasRightChild(self):
        return self._rightChild

    def hasLeftChild(self):
        return self._leftChild

    def setRightChild(self, child):
        self._rightChild = child

    def setLeftChild(self, child):
        self._leftChild = child

    def getLabel(self):
        return self._label

    def isLeaf(self):
        return (not self._leftChild and not self._rightChild)

    def getParent(self):
        return self._parent

    def setParent(self, parent):
        self._parent = parent

    def isRightChild(self):
        return (self.getParent().hasRightChild() and self._label==self._parent._rightChild._label)

    def isLeftChild(self):
        return (self.getParent().hasLeftChild() and self._label==self._parent._leftChild._label)

