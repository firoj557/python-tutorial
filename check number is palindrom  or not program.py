""" Author: Firoj Kumar

 Date: 19-05-2020

This program is check the given number palindrome or not  !"""

x=int(input("Enter a number:"))
temp=x
p=0
while(x>0):
    dig=x%10
    p= p*10+dig
    x=x//10
if(temp==p):
    print('The number {} is palindrome'.format(temp))
else:
    print('The {} Not a palindrome!'.format(temp))




"""output Enter a number=121
          The number 121 is palindrome"""