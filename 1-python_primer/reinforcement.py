# R-1.1 Write a short Python function, is multiple(n, m), that takes two integer
# values and returns True if n is a multiple of m, that is, n = mi for some
# integer i, and False otherwise
def is_multiple(n, m):
    return n % m  == 0

# R-1.2 Write a short Python function, is even(k), that takes an integer value and
# returns True if k is even, and False otherwise. However, your function
# cannot use the multiplication, modulo, or division operators.
def is_even(k):
    return (k & 1) == 0

# R-1.3 Write a short Python function, minmax(data), that takes a sequence of
# one or more numbers, and returns the smallest and largest numbers, in the
# form of a tuple of length two. Do not use the built-in functions min or
# max in implementing your solution
def minmax(data):
    local_max = data[0]
    local_min = data[0]

    for num in data:
        if num >  max:
            max = num
        elif num < min:
            min = num

    return(min, max)

# R-1.4 Write a short Python function that takes a positive integer n and returns
# the sum of the squares of all the positive integers smaller than n.
def sum_of_squares(n):
    if n < 0:
        raise ValueError("number cannot be negative")
    sum = 0
    for num in range(n):
        sum += num*num
    
    return sum


# R-1.5 Give a single command that computes the sum from Exercise R-1.4, rely-
# ing on Python’s comprehension syntax and the built-in sum function.
def sum_of_squares_2(n):
    if n < 0:
        raise ValueError("number cannot be negative")
    
    return sum([k*k for k in range(n)])

# R-1.6 Write a short Python function that takes a positive integer n and returns
# the sum of the squares of all the odd positive integers smaller than n.
def sum_of_squares_odd(n):
    sum = 0
    for num in range(n):
        if num % 2 == 0:
            continue
        sum += num * num
    return sum

# R-1.7 Give a single command that computes the sum from Exercise R-1.6, rely-
# ing on Python’s comprehension syntax and the built-in sum function.
def sum_of_squares_odd2(n):
    if n > 0:
        return sum([k*k for k in range(n) if k % 2 != 0])

# R-1.8 Python allows negative integers to be used as indices into a sequence,
# such as a string. If string s has length n, and expression s[k] is used for in-
# dex −n ≤ k < 0, what is the equivalent index j ≥ 0 such that s[j] references
# the same element?
# my anser: 0 <= j < n


# R-1.9 What parameters should be sent to the range constructor, to produce a
# range with values 50, 60, 70, 80?
range(50, 90, 10)


# R-1.10 What parameters should be sent to the range constructor, to produce a
# range with values 8, 6, 4, 2, 0, −2, −4, −6, −8?
range(8, -9, -2)

# R-1.11 Demonstrate how to use Python’s list comprehension syntax to produce
# the list [1, 2, 4, 8, 16, 32, 64, 128, 256].
[2**k for k in range(9)]

# R-1.12 Python’s random module includes a function choice(data) that returns a
# random element from a non-empty sequence. The random module in-
# cludes a more basic function randrange, with parameterization similar to
# the built-in range function, that return a random choice from the given
# range. Using only the randrange function, implement your own version
# of the choice function.