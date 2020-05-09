""" Author: Firoj Kumar

 Date: 09-05-2020

This program find input number sum and avrage  !"""

x=int(input("enter your number="))
y=float(input("enter your avrage number="))
sum=0
i=1
while i<=x:
    sum=sum+i
    i=i+1
    avg=x/y
    print('the sum of {}  ={} avg {}'.format(x,sum,avg))

    """output enter your number=10
              enter your avrage no=2
              the sum of 10=55 avg=5.0 """