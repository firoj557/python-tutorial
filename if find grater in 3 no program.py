""" Author: Firoj Kumar

 Date: 01-05-2020

This program is find grater in 3 numbers statement  program !"""

a=int(input("enter 1 st no="))
b=int(input("enter 2 nd no="))
c=int(input("enter 3 rd no="))

if (a>b) and (a>c):
    print(a,"is grater")
elif (b>c) and (b>a):
    print(b,"is grater")
else:
    print(c,"is grater")

"""output enter 1 st no=100
          enter 2 nd no=50
          enter 3 rd no=60
          
          100 is grater   """

