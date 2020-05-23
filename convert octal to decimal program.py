""" Author: Firoj Kumar

 Date: 22-05-2020

This program is convert octal into decimal !"""

octal=input("enter your ocatl no=")
if octal=='x':
    exit()
else:
    decimal=str(int(octal,8))
    print(octal,"into decimal",decimal)


"""output
 enter your octal no=745
 745 into decimal 485"""