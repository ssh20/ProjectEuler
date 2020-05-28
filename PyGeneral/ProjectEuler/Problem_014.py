'''
Created on May 26, 2020

@author: 14hoy
'''
from ProjectEuler.BST import Tree

already_done=Tree()
Tree.addNode((1,0))

def collatz_steps(n):
    n=(int(n[0]),n[1])
    if n==(1,0):
        already_done.addNode(already_done.root, (1,0))
    theTuple=already_done.search(1, 0)
    if theTuple!=None:
            return theTuple[1]+1
    else:
        if n%2==0:
            second=collatz_steps(n/2)
            theTuple = (n,second)
            already_done.addNode(theTuple)
        else:
            second=collatz_steps(3*n+1)
            theTuple = (n,second)
            already_done.addNode(theTuple)
        already_done[n]=True
    return theTuple[1]
for i in range(1,1000000):
    collatz_steps((i,0))
print("")
