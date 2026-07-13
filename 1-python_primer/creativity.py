import sys
from random import randint
# C-1.13 Write a function that reverses a list of n
# integers, so that the numbers are listed in the opposite order than they
# were before, and compare this method to an equivalent Python function
# for doing the same thing.
def reverse_2 (my_list):
    reverse_list = []
    for i in range(len(my_list), 0, -1):
        reverse_list.append(my_list[i-1])
    return reverse_list

# C-1.14 Write a short Python function that takes a sequence of integer values and
# determines if there is a distinct pair of numbers in the sequence whose
# product is odd.
def distinct_odd_sum(num_list):
    len_list = len(num_list)
    distinct_pairs = []
    for i in range(len_list):
        for j in range(len_list):    
            if i >= j:
                continue
            if (num_list[i] + num_list[j]) % 2 != 0:
                distinct_pairs.append([num_list[i], num_list[j]])
    return distinct_pairs


# C-1.15 Write a Python function that takes a sequence of numbers and determines
# if all the numbers are different from each other (that is, they are distinct).
def distinct(num_list):
    len_list = len(num_list)
    for i in range(len_list):
        for j in range(len_list):
            if i >= j:
                continue
            if num_list[i] == num_list[j]:
                return False
    return True

# C-1.20 Python’s random module includes a function shuffe(data) that accepts a
# list of elements and randomly reorders the elements so that each possi-
# ble order occurs with equal probability. The random module includes a
# more basic function randint(a, b) that returns a uniformly random integer
# from a to b (including both endpoints). Using only the randint function,
# implement your own version ofe the shuﬄe function.
def shuff(data):
    data_len = len(data)
    generated_list = []
    shuff_list = list(data)
    i = 0
    while len(generated_list) != len(data):
        random_number = randint(0, data_len - 1)
        if generated_list.count(random_number) == 0:
            shuff_list[random_number] = data[i]
            i += 1
            generated_list.append(random_number)
    return shuff_list

# C-1.21 Write a Python program that repeatedly reads lines from standard input
# until an EOFError is raised, and then outputs those lines in reverse order
# (a user can indicate end of input by typing ctrl-D).
def fifo():
    stream_list = []

    print("type something")
    while True:
        try:
            line = input()
            stream_list.append(line)
        except EOFError:
            print("what you typed: \n")
            for i in range(len(stream_list) - 1, 0, -1):
                print(stream_list[i])
            break

# C-1.22 Write a short Python program that takes two arrays a and b of length n
# storing int values, and returns the dot product of a and b. That is, it returns
# an array c of length n such that c[i] = a[i] · b[i], for i = 0, . . . , n − 1.

# C-1.23 Give an example of a Python code fragment that attempts to write an ele-
# ment to a list based on an index that may be out of bounds. If that index
# is out of bounds, the program should catch the exception that results, and
# print the following error message:
# “Don’t try buffer overflow attacks in Python!”

# C-1.24 Write a short Python function that counts the number of vowels in a given
# character string.

# C-1.25 Write a short Python function that takes a string s, representing a sentence,
# and returns a copy of the string with all punctuation removed. For exam-
# ple, if given the string "Let s try, Mike.", this function would return
# "Lets try Mike".

# C-1.26 Write a short program that takes as input three integers, a, b, and c, from
# the console and determines if they can be used in a correct arithmetic
# formula (in the given order), like “a + b = c,” “a = b − c,” or “a ∗ b = c.”

# C-1.27 In Section 1.8, we provided three different implementations of a generator
# that computes factors of a given integer. The third of those implementa-
# tions, from page 41, was the most efﬁcient, but we noted that it did not
# yield the factors in increasing order. Modify the generator so that it reports
# factors in increasing order, while maintaining its general performance ad-
# vantages.

# C-1.28 The p-norm of a vector v = (v1 , v2 , . . . , vn ) in n-dimensional space is de-
# ﬁned as
# 
# p
# v = v1p + v2p + · · · + vnp .
# For the special case of p = 2, this results in the traditional Euclidean
# norm, which represents the length of the vector. For example, the Eu-
# clidean norm of a two-dimensional
# with coordinates (4, 3) has a
# √
# √ vector √
# 2
# 2
# Euclidean norm of 4 + 3 = 16 + 9 = 25 = 5. Give an implemen-
# tation of a function named norm such that norm(v, p) returns the p-norm
# value of v and norm(v) returns the Euclidean norm of v. You may assume
# that v is a list of numbers.