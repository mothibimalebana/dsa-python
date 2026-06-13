# R-1.1 Write a short Python function, is multiple(n, m), that takes two integer
# values and returns True if n is a multiple of m, that is, n = mi for some
# integer i, and False otherwise
def is_multiple(n, m):
    try: 
        return n % m  == 0
    except ZeroDivisionError:
        print("How Swae? You cannot divide by zero")