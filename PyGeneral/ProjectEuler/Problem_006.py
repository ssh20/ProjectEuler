'''
Created on May 21, 2020

@author: 14hoy
'''
upper_lim=100
sum_square=0
for i in range(1,upper_lim+1):
    sum_square=sum_square+i*i
square_sum = (upper_lim*(upper_lim+1)/2)*(upper_lim*(upper_lim+1)/2)
print(str(square_sum-sum_square))