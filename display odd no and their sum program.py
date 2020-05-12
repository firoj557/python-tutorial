""" Author: Firoj Kumar

 Date: 10-05-2020

This program display odd numbers and their sum !"""

x=int(input("enter yor no="))

sum=0
for i in range(x):
    if (i%2!=0):
        print(i)
        sum = sum + i
print('The Sum of odd given Natural Number upto  terms={}'.format(sum))


"""output   enter ypur no= 20
            1
            3
            5
            7
            9
            11
            13
            15
            17
            19
            The sum of odd given Natural no upto term=100
            """

