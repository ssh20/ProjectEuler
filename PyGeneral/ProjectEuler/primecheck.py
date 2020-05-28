'''
Created on May 21, 2020

@author: 14hoy
'''
import math
class primecheck:
    def __init__(self):
        self.prime = 1
    def isprime(self,k):
        for i in range(2,math.floor(math.sqrt(k))+1):
            if k%i==0:
                return False
        
        return True
    @staticmethod
    def sieve(upper_lim):
        primes = [True for i in range(upper_lim + 1)]
        primes[0]=False
        primes[1]=False
        primeslen = len(primes)
        for i in range(2,math.floor(math.sqrt(primeslen))+1):
            if primes[i]:
                j=i+i
                while j<primeslen:
                    primes[j]=False
                    j+=i
        return primes