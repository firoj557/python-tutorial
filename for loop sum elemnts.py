""" Author: Firoj Kumar

 Date: 07-05-2020

This program is for loop sum element  !"""

list=[10,20,30,40,50,60,70,80]

tuple=(90,100,110,120,130,140,150)

set={160,170,180,190,200,210,220}

k=0
p=0
q=0
for i in list:
    k=i+k
    print('list is {} ={}'.format(i,k))


for a in tuple:
    p=a+p
    print('tuple is {} ={}'.format(a,p))


for c in set:
    q=c+q
    print('set is {} ={}'.format(c,q))

"""output   list is 10=10
            list is 20=30
            list is 30=60
            list is 40=100
            list is 50=150
            list is 60=210
            list is 70=280
            list is 80=360
            tuple is 90=90
            tuple is 100=190
            tuple is 110=300
            tuple is 120=420
            tuple is 130=550
            tuple is 140=690
            tuple is 150=840
            set is  160=160
            set is  200=360
            set is  170=530
            set is  210=740
            set is  180=920
            set is  220=1140
            set is  190=1330 """