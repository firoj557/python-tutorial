""" Author: Firoj Kumar

 Date: 22-05-2020

This program is convert decimal into octal !"""

num=int(input("enter your number="))

temp=num
sum=0
i=1
while temp!=0:
    rem=int(temp%8)
    sum=sum+i*rem
    i=i*10
    temp=temp/8
print(sum)


"""output
    enter your number=79
    117
    """
