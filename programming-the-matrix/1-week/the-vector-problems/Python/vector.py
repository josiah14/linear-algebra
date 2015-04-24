from functools import reduce
from itertools import count

def add(*vectors):
    return [ reduce(lambda x0, x1: x0 + x1, xs) for xs in zip(*vectors) ]

def minus(*vectors):
    return [ reduce(lambda x0, x1: x0 - x1, xs) for xs in zip(*vectors) ]

def scalar_mult(constant, vector):
    return list(map(lambda x: constant * x, vector))

def inverse_factorial(num):
    for i in count(1):
        num = num / i
        if num == 1: return i
        if num < 1: raise ValueError("number was not an even factorial.")

def inverse_natural_sum(num, start):
    for i in range(start, 0, -1):
        num = num - i
        if num == 0: return i
        if num < 0: raise ValueError("number is not a natural sum.")
    
def permutations_unordered_no_repeat(collection):
    def reducer(acc, x):
        if acc == collection[0]:
            return [ (acc, y) for y in collection[1:] ] + [ (x, y) for y in collection[2:] ]
        else:
            start_index = len(collection) - 1 - inverse_natural_sum(len(acc), len(collection) - 1) + 2
            return acc + [ (x, y) for y in collection[start_index:] ]
    return reduce(reducer, collection)

def flatten2(collection):
    return [ y for x in collection for y in x ]
        
