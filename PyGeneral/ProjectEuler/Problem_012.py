'''
Created on May 26, 2020

@author: 14hoy
'''
import math
def get_divisors(n):
    count = 0
    for i in range(1,math.ceil(math.sqrt(n))):
        if n%i==0:
            if i!=math.sqrt(n):
                count +=2
            else:
                count+=1
    return count

breakwhile = False
n=1
while(~breakwhile):
    trinum = n*(n+1)/2
    num_of_divisors = get_divisors(trinum)
    if get_divisors(trinum)>500:
        print("The first triangular number with over 500 divisors is "+str(trinum)+".")
        breakwhile = True
    n+=1