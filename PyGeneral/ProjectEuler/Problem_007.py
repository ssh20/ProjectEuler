'''
Created on May 21, 2020

@author: 14hoy
'''
import math
def isitprime(k):
    for i in range(2,math.floor(math.sqrt(k))+1):
        if k%i==0:
            return False
    
    return True

count = 0
nth_prime=1
lim=10001
while count<lim:
    i = nth_prime+1
    found_prime=False
    while not found_prime:
        if isitprime(i):
            nth_prime = i
            found_prime=True
        i=i+1
    count=count+1
    
print(str(nth_prime))