'''
Created on May 20, 2020

@author: 14hoy
'''
for i in range(999,1,-1):
    for j in range(999,1,-1):
        if str(i*j)==str(i*j)[::-1]:
            print(str(i*j)+", "+str(i)+"*"+str(j))
            break