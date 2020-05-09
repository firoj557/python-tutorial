""" Author: Firoj Kumar

 Date: 02-05-2020

This program is check the enter charactor is alphabet or not !"""

x=input("enter a charactor=")

if (x>='a' and x <='z') or (x>='A' and x<='Z'):
    print(x,"is alphabet")
else:
    print(x,"is not alphabet")

"""output entre a charctor = b
          b is a alphabet 
          
          enter a charactor= D
          D is a alphabet 
          
          enter a charactor=10
          10 is not a alphabet     """