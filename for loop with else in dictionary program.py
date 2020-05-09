""" Author: Firoj Kumar

 Date: 08-05-2020

This program is for loop print dectionary element  !"""

x=input("enter your student name=")

marks={'firoj':50,'rakesh':70,'umesh':30,'rajesh':55,'roshan':20}

for student in marks:
    if student==x:
        print(marks[student])
        break

    else:
        print("student name not found")






        """output enter your student name=firoj
                   50
           output enter your student name=hitesh
                  student name not found"""

