""" Author: Firoj Kumar

 Date: 02-05-2020

This program is check enter alphabet is lowercase or uppercase program !"""

x= input("enter any alphabet =")

if (x>='a' and x<="z"):
    print(x,"alphabet is lower case")
elif(x>='A' and x<='Z'):
    print(x,"alphabet is upper case")
else:
    print("invalid enter")
