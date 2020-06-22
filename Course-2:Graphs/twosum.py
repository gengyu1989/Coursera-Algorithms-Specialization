#!/usr/bin/python3

"""
The goal of this problem is to implement a variant of the 2-SUM algorithm
covered in this week's lectures. The file contains 1 million integers,
both positive and negative (there might be some repetitions!).This is your array of integers,
with the ith row of the file specifying the ith entry of the array.

Your task is to compute the number of target values t in the interval [-10000,10000] (inclusive)
such that there are distinct numbers x,y in the input file that satisfy x+y=t.
(NOTE: ensuring distinctness requires a one-line addition to the algorithm from lecture.)

Write your numeric answer (an integer between 0 and 20001) in the space provided.

OPTIONAL CHALLENGE: If this problem is too easy for you, try implementing your own hash table for it.
For example, you could compare performance under the chaining and open addressing approaches
to resolving collisions.


Problem Answer: 427


NOTE: sets in python are like dicts with dummy values, so under the hood it's a hash table, thus
providing O(1) look ups and insertions on average, like hash tables
https://docs.python.org/3/library/stdtypes.html#set
"""

