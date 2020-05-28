'''
Created on May 21, 2020

@author: 14hoy
'''
import math
for a in range(1,999):
    b=1000*(a-500)/(a-1000)
    if math.floor(b)==b:
        c=1000-a-b
        print("The solution is ("+str(a)+", "+str(b)+", "+str(c)+")")
        break