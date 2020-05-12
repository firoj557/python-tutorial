""" Author: Firoj Kumar

 Date: 10-05-2020

This program print pattern  !"""

x=5
for i in range(0,x):
    for j in range(0,x-i-1):
        print(end=" ")
    for j in range(0,i+1):
        print("*",end=" ")
    print( )



"""output     *
             * *
            * * *
           * * * * 
          * * * * *   """