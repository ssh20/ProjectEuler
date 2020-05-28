'''
Created on May 20, 2020

@author: 14hoy
'''
the_sum=0
for i in range(1000):
    if i%3==0 or i%5==0:
        the_sum=the_sum+i
print(the_sum)