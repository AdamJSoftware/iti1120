import math


def repeater(s1, s2, n):
    return "_"+(s1+s2)*n+"_"


def roots(a, b, c):
    root1 = (-b+math.sqrt(b**2-4*a*c)) / 2*a
    root2 = (-b-math.sqrt(b**2-4*a*c)) / 2*a
    print("The quadratic equation with coefficients a = " + str(a) + " b = " +
          str(b) + " c = " + str(c) + " has the following solutions (i.e. roots):")
    print(str(root1) + " and " + str(root2))


def real_roots(a, b, c):
    return b**2-4*a*c >= 0


def reverse(x):
    return int(str(x % 10)+str(x // 10))
