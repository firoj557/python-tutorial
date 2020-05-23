""" Author: Firoj Kumar

 Date: 22-05-2020

This program is convert decimal into hexadecimal !"""

decimal=input("enter your decimal no=")
if decimal=='x':
    exit()
else:
    temp=int(decimal)
    hex=hex(temp)

    print(decimal,"into hexadecimal=",hex)


"""output
 enter your decimal no= 79
 79 into hexadecimal 4f"""