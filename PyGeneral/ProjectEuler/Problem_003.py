'''
Created on May 20, 2020

@author: 14hoy
'''
import math


def isitprime(k):
    for i in range(2,math.floor(math.sqrt(k))+1):
        if k%i==0:
            return False
    
    return True

n=600851475143
lim = math.sqrt(n)
maxprime=0
for i in range(2,math.floor(lim)):
    if n%i==0:
        if isitprime(n/i):
            maxprime=n/i
            print("The maximum prime divisor of "+str(n)+" is "+str(maxprime))
            break
        elif isitprime(i):
                maxprime = i
print("The maximum prime divisor of "+str(n)+" is "+str(maxprime))