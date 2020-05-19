""" Author: Firoj Kumar

 Date: 19-05-2020

This program is reverce order of given number  !"""

num = int(input("Enter your number: "))

i = 0

while (num > 0):
    # Logic
    remainder = num % 10
    i = i*10 + remainder
    num = num // 10
print("The reverse number is : {}".format(i))

""" output  Enter your no= 12345
            The revers no is:54321
            """