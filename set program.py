""" Author: Firoj Kumar

 Date: 26-04-2020

This program is set initialization!"""

x={10,20,30,40,50,'hitesh','rakesh',2.0,100,}
print("x=",x)
"""output=x={10,20,30,40,50,'hitesh','rakesh',2.0,100,}"""

"""(1)Not support dubling value"""
x={10,20,30,40,50,'hitesh','rakesh',2.0,100,100}
print("x=",x)
"""output=x={10,20,30,40,50,'hitesh','rakesh',2.0,100,}"""

"""(2)type() use on set"""
print(type(x))
"""output = <class 'set'>"""

"""(3) print spacific elements"""
print(x[1])
""" output=TypeError: 'set' object does not support indexing"""

"""(4) immutable-not support change the values"""
x[1]=150
print(x)
""" output=TypeError: 'set' object does not support indexing"""


"""(5)Not support specilize : opretor"""
print(x[1:])
print(x)
""" output=TypeError: 'set' object does not support indexing"""

