'''
Created on May 21, 2020

@author: 14hoy
'''
def gcd(a,b):
    if a==0:
        return b
    if b==0:
        return a
    if a>b:
        return gcd(a%b,b)
    return gcd(a,b%a)

upper_lim=20
rolling_num=1
for i in range(1,upper_lim):
    the_gcd=gcd(i,rolling_num)
    rolling_num=rolling_num*i/the_gcd

print(rolling_num)