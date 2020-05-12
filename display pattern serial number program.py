""" Author: Firoj Kumar

 Date: 10-05-2020

This program print pattern  !"""

x=4
no=0
for row in range(1,x+1):
    for column in range(1,row+1):
        no=no+1
        print('{}'.format(no),end=" ")
    print( )

    """output   1
                2 3
                4 5 6 
                7 8 9 10"""