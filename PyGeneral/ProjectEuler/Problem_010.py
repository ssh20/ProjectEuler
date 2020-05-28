'''
Created on May 21, 2020

@author: 14hoy
'''
from ProjectEuler.primecheck import primecheck as pc
the_sum = 0
upper_lim=2000000;
primechecker = pc()
primes = pc.sieve(upper_lim)
for i in range(len(primes)):
    if primes[i]:
        the_sum+=i
print("The sum is "+str(the_sum))