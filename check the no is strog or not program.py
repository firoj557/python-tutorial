""" Author: Firoj Kumar

 Date: 22-05-2020

This program is check the given no is strong or not  !"""

Number = int(input(" Please Enter any Number: "))
Sum = 0
Temp = Number

while (Temp > 0):
    F = 1
    i = 1
    Reminder = Temp % 10

    while (i <= Reminder):
        F = F * i
        i = i + 1

    Sum = Sum + F
    Temp = Temp // 10

if (Sum == Number):
    print(" %d is a Strong Number" % Number)
else:
    print(" %d is not a Strong Number" % Number)


"""output
     Please enter any number=145
     145 is a strong Number  """