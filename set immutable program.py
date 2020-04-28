""" Author: Firoj Kumar

 Date: 28-04-2020

This program is set immutable  !"""

x={10,20,30,40,50,'hitesh','rakesh',2.0,100,}

""" immutable-not support change the values"""
x[1]=150
print(x)
""" output=TypeError: 'set' object does not support indexing"""