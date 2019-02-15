'''
Created on 10 Dec 2018

@author: Administrator
'''

class Person(object):
    '''
    classdocs
    '''

    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def myInfo(self):
        print ( "My name is " + self.name, "My age is " + str(self.age))
        
        
p1 = Person("Fred",21)
p1.myInfo()
#print (p1.age, p1.name)
        