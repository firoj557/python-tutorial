""" Author: Firoj Kumar

 Date: 01-05-2020

This program is check no divisible 5 and 11 or not !"""

x=int(input("enter your no="))
if (x%5==0):
    print("no is divisible on 5=",x)
elif(x%11==0):
    print("no is divisible on 11=",x)
else:
    print("no is not divisible on 5 and 11=",x)

"""output enter your no=20
          no is divisible on 5=20
          
          enter your no =22
          no is divisible on 11=22
          
          enter your no=16
          no is not divisible 5 and 11=16"""