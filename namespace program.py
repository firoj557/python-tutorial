""" Author: Firoj Kumar

 Date: 01-05-2020

This program is namespace in memory  program !"""

x=50
print("id(50)=",id(50))

print("id(x)=",id(x))

x=x-1
print("id(49)=",id(49))

print("id(x)=",id(x))

y=50
print("id(y)=",id(y))

print("id(50)=",id(50))

"""output id(50)=10916064
          id(x)= 10916064
          id(49)=10916032
          id(x) =10916032
          id(y)=10916064
          id(50)=10916064
          """
