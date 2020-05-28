'''
Created on May 27, 2020

@author: 14hoy
'''
class TreeNode:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.data = value

class Tree:
    def __init__(self):
        self.root = None

    def addNode(self, node, value):
        if(node==None):
            self.root = TreeNode(value)
        else:
            if(value<node.data):
                if(node.left==None):
                    node.left = TreeNode(value)
                else:
                    self.addNode(node.left, value)
            else:
                if(node.right==None):
                    node.right = TreeNode(value)
                else:
                    self.addNode(node.right, value)
    def search(self,root,key): 
      
    # Base Cases: root is null or key is present at root 
        if root is None or root.data == key: 
            return root 
      
        # Key is greater than root's key 
        if root.data < key: 
            return self.search(root.right,key) 
        
        # Key is smaller than root's key 
        return self.search(root.left,key) 

    def printInorder(self, node):
        if(node!=None):
            self.printInorder(node.left)
            print(node.data)
            self.printInorder(node.right)

