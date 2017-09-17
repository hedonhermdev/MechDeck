from fractions import Fraction
import math
def series1(n):
    if n == 1:
        return 1/2
    else:
        print(Fraction(n-1, n+1))
        return ((n - 1)/(n + 1)) * series1(n -1)

array1 = [Fraction(series1(x)).limit_denominator(100) for x in range(1, 10)]


def fibonnacci(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fibonnacci(n - 1) + fibonnacci(n - 2)

def sum_fib(n):
    return fibonnacci(n + 2) - 1

def square_diff(n):
    s1_squared = (n*(n + 1)//2)**2
    s2 = n*(n+1)*(2*n + 1)//6
    return s1_squared - s2

def npr(n, r):
    return math.factorial(n)//math.factorial(n-r)
def ncr(n, r):
    numr = 1
    for i in range(n, r-1, -1):
        numr *= i
    denr = 1
    for i in range(1, r + 1):
        denr *= i
    return numr//denr


print(ncr(100, 99))
