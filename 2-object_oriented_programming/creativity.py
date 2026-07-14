# C-2.24 Suppose you are on the design team for a new e-book reader. What are the
# primary classes and methods that the Python software for your reader will
# need? You should include an inheritance diagram for this code, but you
# do not need to write any actual code. Your software architecture should
# at least include ways for customers to buy new books, view their list of
# purchased books, and read their purchased books.

# C-2.25 Exercise R-2.12 uses the mul method to support multiplying a Vector
# by a number, while Exercise R-2.14 uses the mul method to support
# computing a dot product of two vectors. Give a single implementation of
# Vector. mul that uses run-time type checking to support both syntaxes
# u v and u k, where u and v designate vector instances and k represents
# a number.

# C-2.26 The SequenceIterator class of Section 2.3.4 provides what is known as a
# forward iterator. Implement a class named ReversedSequenceIterator that
# serves as a reverse iterator for any Python sequence type. The first call to
# next should return the last element of the sequence, the second call to next
# should return the second-to-last element, and so forth.
# www.it-ebooks.info
# 106 Chapter 2. Object-Oriented Programming

# C-2.27 In Section 2.3.5, we note that our version of the Range class has implicit support for iteration, due to its explicit support of both len
# and getitem . The class also receives implicit support of the Boolean
# test, “k in r” for Range r. This test is evaluated based on a forward iteration through the range, as evidenced by the relative quickness of the test
# 2 in Range(10000000) versus 9999999 in Range(10000000). Provide a
# more efficient implementation of the contains method to determine
# whether a particular value lies within a given range. The running time of
# your method should be independent of the length of the range.

# C-2.28 The PredatoryCreditCard class of Section 2.4.1 provides a process month
# method that models the completion of a monthly cycle. Modify the class
# so that once a customer has made ten calls to charge in the current month,
# each additional call to that function results in an additional $1 surcharge.

# C-2.29 Modify the PredatoryCreditCard class from Section 2.4.1 so that a customer is assigned a minimum monthly payment, as a percentage of the
# balance, and so that a late fee is assessed if the customer does not subsequently pay that minimum amount before the next monthly cycle.

# C-2.30 At the close of Section 2.4.1, we suggest a model in which the CreditCard
# class supports a nonpublic method, set balance(b), that could be used
# by subclasses to affect a change to the balance, without directly accessing
# the balance data member. Implement such a model, revising both the
# CreditCard and PredatoryCreditCard classes accordingly.

# C-2.31 Write a Python class that extends the Progression class so that each value
# in the progression is the absolute value of the difference between the previous two values. You should include a constructor that accepts a pair of
# numbers as the first two values, using 2 and 200 as the defaults.

# C-2.32 Write a Python class that extends the Progression class so that each value
# in the progression is the square root of the previous value. (Note that
# you can no longer represent each value with an integer.) Your constructor should accept an optional parameter specifying the start value, using
# 65,536 as a default.