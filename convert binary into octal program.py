""" Author: Firoj Kumar

 Date: 22-05-2020

This program is convert binary into octal !"""

binary=input("enter your binary no=")
if binary=='x':
    exit()
else:
    temp=int(binary,2)

    print(binary,"into octal",oct(temp))


"""output
 enter your binary no=1001
 1001 into octal 11"""