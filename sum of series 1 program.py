""" Author: Firoj Kumar

 Date: 17-05-2020

This program is sum of series 1+11+111+1111....1n !"""

x=int(input("enter the series number="))
sum=0
t=1
i=0
r=t
for i in range(x):
    sum=sum+t
    i=i+1

    print('the sum of 1+{} series value  ={}'.format(t,sum))
    t = t * 10 + r

    """output :
       enter the serie number=5
       the sum of 1+1 series value=1
       the sum of 1+11 series value=12
       the sum of 1+111 series value=123
       the sum of 1+1111 series value=1234
       the sum of 1+11111 series value=12345"""
