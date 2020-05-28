'''
Created on May 20, 2020

@author: 14hoy
'''
thing1=1
thing2=2
the_sum=0
while thing1<4000000 and thing2 < 4000000:
    if thing1%2==0:
        the_sum=the_sum+thing1
    if thing2%2==0:
        the_sum=the_sum+thing2
    thing1=thing1+thing2
    thing2=thing2+thing1
print(the_sum)