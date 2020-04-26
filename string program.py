""" Author: Firoj Kumar

 Date: 26-04-2020

This program is string  initialization!"""

a='firoj kumar'
print(a)
"""output = firoj kumar"""

"""(1) print spacific charactor in a string"""
print(a[0],a[4])
"""output= f j"""


"""(2) print a sting  single ' ' quote"""
print(" 'firoj kuamr' ")
"""output = 'firoj kumar' """

"""(3) print a string in dobule quote"""
print(' "firoj kumar" ')
"""output = "firoj kumar" """


"""(4) print a string in multiline quote"""

print(' """firoj kumar""" ')

 """output-firoj kuamr"""



"""(5) print a other string in single quote """
print(a," 'hello world' ")
"""output= firoj kumar 'hello world' """



"""(6) immutable- change the string corrector """

a[2]='n'
print(a)
"""output- TypeError: 'str' obj doe not support ittem assigment"""