'''
Created on 13 Dec 2018

@author: Administrator
'''
cardNo = "6304024062814363"

cardSum = 0
cardLen = len ( cardNo )
print ("Odd")
for n in range ( 1 , cardLen, 2 ) :
    print (n, cardNo[n])
    x = int(cardNo[n])
    cardSum = cardSum + x
    
print("Even")
for n in range ( 0 , cardLen, 2 ) :
    print (n, cardNo[n])
    x = int(cardNo[n]) * 2
    if x > 9 :
        x = x - 9
    cardSum = cardSum + x 
   
print(cardSum)
print (cardSum % 10 )
if ( cardSum % 10 == 0 ) :
    print ("Valid Card")
else :
    print ("Whoops Invalid Card!")  