""" Author: Firoj Kumar

 Date: 22-05-2020

This program is octal into binary !"""

octal=input("enter your octal no=")
if octal=='x':
    exit()
else:
    temp=int(octal,8)

    print(octal,"into binary",bin(temp))


"""output
 enter your octal no=57
 57 into binary 101111"""