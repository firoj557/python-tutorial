""" Author: Firoj Kumar

 Date: 19-05-2020

This program is check the no perfact or not"""


x=int(input("enter your no="))
sum=0
for i in range(1,x):
    if x%i==0:
        sum=sum+i
        print(i)
if sum==x:
    print("no is perfact no=",x)
else:
    print("no is not perfact no=",x)


"""output 
 enter your no=6
 1
 2
 3
no is perfact no=6
 
 enter your no=4
1
2
  no is not perfact=4"""



































































































