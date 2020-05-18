""" Author: Firoj Kumar

 Date: 18-05-2020

This program check number is prime or not  !"""

x=int(input("enter your number="))

for i in range(2,x):
    if x%i==0:
        print('{} is not prime number'.format(x))
        break

else:
    print('{} is a prime number'.format(x))

    """output 
    
       enter your number=13
       13 is a prime number
       
       enter your number=49
       49 is not a prime number """


