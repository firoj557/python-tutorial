""" Author: Firoj Kumar

 Date: 10-05-2020

This program print pattern  !"""

x=4
no=0
for i in range(0,x):
    for j in range(0,x-i-1):
        print(end=" ")
    for j in range(0,i+1):
        no=no+1
        print('{}'.format(no),end=" ")
    print( )


"""output   1
           2 3
          4 5 6
         7 8 9 10     """