""" Author: Firoj Kumar

 Date: 01-05-2020

This program is count total no of notes program !"""

a=int(input("enter rupees 10 note="))
t=10*a

b=int(input("enter rupees 20 note="))
v=20*b

c=int(input("enter rupees 50note="))
w=50*c

d=int(input("enter rupees 100 note="))
x=100*d

e=int(input("enter rupees 200 note="))
y=200*e

f=int(input("enter rupees 500 note="))
z=500*f



print('Note 10 x{}={}'.format(a,t))
print('Note 20 x{}={}'.format(b,v))
print('Note 50 x{}={}'.format(c,w))
print('Note 100 x{}={}'.format(d,x))
print('Note 200 x{}={}'.format(e,y))
print('Note 500 x{}={}'.format(f,z))
p=t+v+w+x+y+z
print("total amount is =",p)

"""output enter rupees 10 note=2
          enter rupees 20 note=2
          enter rupees 50 note=2
          enter rupees 100 note=2
          enter rupees 200 note=2
          enter rupees 500 note=2
          
          Note 10x2=20
          Note 20x2=40
          Note 50x2=100
          Note 100x2=200
          Note 200x2=400
          Note 500x2=1000
          total amount is =1760  """
