""" Author: Firoj Kumar

 Date: 18-05-2020

This program print pattern  !"""

x=int(input("enter your number="))
for row in range(1,x+1):
    for column in range(1,row+1):
        print("*",end=" ")
    print( )

for row in range(x+1,0,-1):
    for column in range(1,row+1):
        print("*",end=" ")
    print( )
"""outpur   *
            **
            ***
            ****
            *****
            ****
            ***
            **
            *  """