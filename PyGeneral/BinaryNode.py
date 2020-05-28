class BinaryNode:
    def __init__(self, nodeData = None, leftChild = None,
                 rightChild = None):
        if leftChild is not None:
            try:
                assert leftChild.getData().type() is nodeData.type()
            except:
                raise TypeError('Left child is not of proper type')
        if rightChild is not None:
            try:
                assert rightChild.getData().type() is nodeData.type()
            except:
                raise TypeError('Right child is not of proper type')
        self.nodeData = nodeData
        self.leftChild = leftChild
        self.rightChild = rightChild
        
    def getData(self):
        return self.nodeData
    def setData(self, nodeData):
        self.nodeData = nodeData
    
    def getLeftChild(self):
        return self.leftChild
    def setLeftChild(self, leftChild):
        self.leftChild = leftChild
    def hasLeftChild(self):
        return self.leftChild!=None
    
    def getRightChild(self):
        return self.rightChild
    def setRightChild(self, rightChild):
        self.rightChild = rightChild
    def hasRightChild(self):
        return self.rightChild!=None
    
    def isLeaf(self):
        return self.leftChild==None and self.rightChild==None
    
class Main:
    node1 = BinaryNode("hello", BinaryNode("goodbye"))
