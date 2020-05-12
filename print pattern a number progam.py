""" Author: Firoj Kumar

 Date: 10-05-2020

This program print pattern  !"""

x=4
for row in range(1,x+1):
    for column in range(1,row+1):
        print(column,end=" ")
    print( )


"""output   1
            1 2
            1 2 3
            1 2 3 4    """