""" Author: Firoj Kumar

 Date: 01-05-2020

This program is check month of days program !"""

x = int(input("enter month no="))

if x==1:
    print(x,"this month is january days of=31")
elif x==2:
    print(x, "this month is feburary days of=28-(29leep year)")
elif x==3:
    print(x, "this month is march days of =31")
elif x==4:
    print(x, "this month is april days of =30")
elif x==5:
    print(x, "this month is may days of =31")
elif x==6:
    print(x, "this month is jun days of =30")
elif x==7:
    print(x, "this month is july days of =31")
elif x==8:
    print(x, "this month is agust days of =31")
elif x==9:
    print(x, "this month is september days of =30")
elif x==10:
    print(x, "this month is october days of =31")
elif x==11:
    print(x, "this month is november days of =30")
elif x==12:
    print(x, "this month is December days of =31")
else:
    print(x, "this month  number is invalid ")


"""output  etner month no= 5
           5 this month is may days of =31
           
           enter month no =15
           15 this month no is invalid """