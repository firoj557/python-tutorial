""" Author: Firoj Kumar

 Date: 18-05-2020

This program check number is prime or not  !"""

x=int(input("enter your start  number="))
y=int(input("enter your end number="))

for i in range(x,y+1):
    if i>1:
        for num in range(2,i):
            if i%num==0:

                break


        else:
            print('{} is prime no'.format(i))

"""output enter your start number=1
          enter your end number=50
          2 is prime number
          3 is prime number
          5 is prime number
          7 is prime number
          11 is prime number
          13 is prime number
          17 is prime number
          19 is prime number
          23 is prime number
          29 is prime number
          31 is prime number
          37 is prime number
          41 is prime number
          47 is prime number
          """