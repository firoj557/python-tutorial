""" Author: Firoj Kumar

 Date: 18-05-2020

This program check armstong no given range  !"""
x=int(input("enter your start no="))
y=int(input("enter your end number"))

for i in range(x,y+1):
    num=i
    result=0
    n=len(str(i))
    while(i>0):
        digit=i%10
        result=result+digit**n
        i=i//10
    if num==result:
        print('{} number is armstrong'.format(num))


"""output  enter your start no=1
           enter your end no=1000
           1 is armstrong no
           2 is armstrong no
           3 is armstrong no
           4 is armstrong no
           5 is armstrong no
           6 is armstrong no
           7 is armstrong no
           8 is armstrong no
           9 is armstrong no
           153 is armstrong no
           370 is armstrong no
           371 is armstrong no
           407 is armstrong no"""