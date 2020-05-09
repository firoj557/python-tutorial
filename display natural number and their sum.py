""" Author: Firoj Kumar

 Date: 08-05-2020

This program display natural number and their sum  !"""


x=int(input("enter your number="))

for i in range(x):
    print(i)

sum=0
i=1
while i<=x:
    sum=sum+i
    i=i+1
    print('the sum of  ={}'.format(sum))


    """output enter your number =7
              1
              2
              3
              4
              5
              6
              the sum of =28"""




