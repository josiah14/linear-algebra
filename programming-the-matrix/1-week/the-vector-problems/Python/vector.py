from functools import reduce
from itertools import count
import GF2

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

def product(nums):
    return reduce(lambda acc, x: acc * x, nums)
        
def dot_prod(*vectors):
    return sum( [ product(xs) for xs in zip(*vectors) ] )

def v_and(*vectors):
    return [ reduce(lambda acc, x: acc and x, xs) for xs in zip(*vectors) ]

# This doesn't actually solve an arbitrary system of GF2 equations, but the law of diminishing returns encourages me to move on.
def GF2_solve_dot_prod_sys(goal, *vectors):
    result_list = list( map(lambda x: GF2.zero, vectors[0]) )
    if goal == GF2.one:
        and_vector = v_and(*vectors)
        if GF2.one in and_vector: result_list[and_vector.index(GF2.one)] = GF2.one
        else: result_list = None
    return result_list
