""" Author: Firoj Kumar

 Date: 10-05-2020

This program display odd numbers and their sum !"""

x=int(input("enter yor no="))

sum=0
for i in range(x+1):
    if (i%2==0):
        print(i)
        sum = sum + i

print('The Sum of sum Natural Number upto terms={}'.format(sum))

"""output  enter your no= 20
           0
           2
           4
           6
           8
           10
           12
           14
           16
           18
           20
           The sum of Naturan given no upto term=110
           """