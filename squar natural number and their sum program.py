""" Author: Firoj Kumar

 Date: 11-05-2020

This program square natural number and their sum  !"""

x=int(input("enter your number="))
sum=0
s=0
for i in range(1,x+1):
    s=i**2
    sum=sum+s
    print('The {} square natural number are {} sum= {}'.format(i,s,sum))


"""output enter your no= 5
          the 1 square natural number are 1 sum=1
          the 2 square natural number are 4 sum=5
          the 3 square natural number are 9 sum=14
          the 4 square natural number are 16 sum=30
          the 5 square natural number are 25 sum=55  """
