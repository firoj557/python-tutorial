""" Author: Firoj Kumar

 Date: 18-05-2020

This program check the given number is armstrong or not  !"""
x=int(input("enter your number="))

for i in range(1,x+1):
    num=i
    result=0
    n=len(str(i))
    while(i!=0):
        digit=i%10
        result=result+digit**n
        i=i//10
if num==result:
    print('{} number is armstrong'.format(num))

else:
    print('{} is not armstrong'.format(num))

"""output enter your no=153
   153 is armstrong """
