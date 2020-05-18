""" Author: Firoj Kumar

 Date: 17-05-2020

This program is sum of series 9 +99 +999....9n !"""

x=int(input("enter the series number="))
sum=0
t=9
i=0
r=t
for i in range(x):
    sum=sum+t
    i=i+1

    print('the sum of 9+{} series value  ={}'.format(t,sum))
    t = t * 10 + r

    """ output :
        enter the servie number= 5
        the sum of 9+9 series value=9
        the sum of 9+99 series value=108
        the sum of 9+999 series value=1107
        the sum of 9+9999 series value=11106
        the sum of 9+99999 series value=111105
        """

