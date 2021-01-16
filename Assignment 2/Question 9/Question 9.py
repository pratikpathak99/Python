#9.	Write a function called root that is given a number x and an integer n and returns x power 1/n. In the function deﬁnition,
# set the default value of n to 2.

import math
def root(x,n=2):

    return math.pow(x, 1) / n

o = root(16)
print(o)
