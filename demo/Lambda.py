'''
Created on 10 Dec 2018

@author: Administrator
'''
def myfunc(n):
    return lambda a : a * n 



x = myfunc(2)
y = myfunc(3)

print ( x ( 10 ))
print ( y (10 ))

z = lambda a : a 
print (z(999) )