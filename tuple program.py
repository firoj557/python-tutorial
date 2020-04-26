""" Author: Firoj Kumar

 Date: 25-04-2020

This program is Tuple initialization!"""

t = (10,20,30,40,50,'firoj', 1+3j,10.5,90,100)
print("t = ", t[0:])

"""Output t =(10,20,30,40,50,'firoj', 1+3j,10.5,90,100)"""


"""(1)print 3rd no elements"""
print("t[3] = ", t[3])
"""Output t[3] = 40 """


"""(2) print element using slizing oprator"""
print("t[0:2] = ", t[0:2])
"""Output t[0:1] =(10 20)"""


"""(3) print 5 element store in tuple """
print("t[0:5]=" , t[0:5])
"""output t[0:5]=(10,20,30,40,50)"""




"""(4) print specific values in tuple"""

print("t[]", t[2],t[4],t[6],t[8])

"""output t[ ]= 30 50 (1+3j) 90"""



"""(5) print reverce elements"""

print("t[]",t[ :9])

"""output t[ ]= (10,20,30,40,50,'firoj', (1+3j),10.5,90)"""



"""(6) immutable tuple elements"""

t[4]=110
print("t[4] =",t[4])

"""Output= t[4]=110
TypeError: 'tuple' object does not support item assignment"""



