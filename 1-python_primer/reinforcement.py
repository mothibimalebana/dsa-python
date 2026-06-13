# R-1.1 Write a short Python function, is multiple(n, m), that takes two integer
# values and returns True if n is a multiple of m, that is, n = mi for some
# integer i, and False otherwise
def is_multiple(n, m):
    return n % m  == 0

# R-1.2 Write a short Python function, is even(k), that takes an integer value and
# returns True if k is even, and False otherwise. However, your function
# cannot use the multiplication, modulo, or division operators.
def is_even(k):
    if k == 1:
        return False
    num = bin(k)
    return True if (num[-1] == '0' and k != 1) else False
