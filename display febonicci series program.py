""" Author: Firoj Kumar

 Date: 19-05-2020

This program display febonnicci series  !"""
# Program to display the Fibonacci sequence up to n-th term

x = int(input("enetr your number "))

# first two terms
a, b = 0, 1
count = 0

# check if the number of terms is valid
if x <= 0:
   print("Please enter a positive number")
elif x == 1:
   print("Fibonacci sequence upto",x,":")
   print(a)
else:
   print("Fibonacci sequence:")
   while count < x:
       print(a)
       c = a + b
       # update values
       a = b
       b = c
       count += 1

       """ enter your no=10
          febonicci sequence
          1
          1
          2
          3
          5
          8
          13
          21
          34
          """