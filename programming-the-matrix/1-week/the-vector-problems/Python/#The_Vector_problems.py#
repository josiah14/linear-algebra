import vector
import GF2

# version code ef5291f09f60+
coursera = 1
# Please fill out this stencil and submit using the provided submission script.

# Some of the GF2 problems require use of the value GF2.one so the stencil imports it.

from GF2 import one

## 1: (Problem 1) Vector Addition Practice 1
#Please express each answer as a list of numbers
p1_v = [-1, 3]
p1_u = [0, 4]
p1_v_plus_u = vector.add(p1_v, p1_u)
p1_v_minus_u = vector.minus(p1_v, p1_u)
p1_three_v_minus_two_u = vector.minus(vector.scalar_mult(3, p1_v), vector.scalar_mult(2, p1_u))

## 2: (Problem 2) Vector Addition Practice 2
p2_u = [-1,  1, 1]
p2_v = [ 2, -1, 5]
p2_v_plus_u = vector.add(p2_v, p2_u)
p2_v_minus_u = vector.minus(p2_v, p2_u)
p2_two_v_minus_u = vector.minus(vector.scalar_mult(2, p2_v), p2_u)
p2_v_plus_two_u = vector.add(p2_v, vector.scalar_mult(2, p2_u))

## 3: (Problem 3) Vector Addition Practice 3
p3_v = [GF2.zero, GF2.one, GF2.one]
p3_u = [GF2.one, GF2.one, GF2.one]
p3_vector_sum_1 = vector.add(p3_v, p3_u)
p3_vector_sum_2 = vector.add(p3_v, p3_u, p3_u)

## 4: (Problem 4) GF2 Vector Addition A
# Please express your solution as a subset of the letters {'a','b','c','d','e','f'}.
# For example, {'a','b','c'} is the subset consisting of:
#   a (1100000), b (0110000), and c (0011000).
# The answer should be an empty set, written set(), if the given vector u cannot
# be written as the sum of any subset of the vectors a, b, c, d, e, and f.
p4_vectors = {
    'a': [GF2.one, GF2.one, GF2.zero, GF2.zero, GF2.zero, GF2.zero, GF2.zero],
    'b': [GF2.zero, GF2.one, GF2.one, GF2.zero, GF2.zero, GF2.zero, GF2.zero],
    'c': [GF2.zero, GF2.zero, GF2.one, GF2.one, GF2.zero, GF2.zero, GF2.zero],
    'd': [GF2.zero, GF2.zero, GF2.zero, GF2.one, GF2.one, GF2.zero, GF2.zero],
    'e': [GF2.zero, GF2.zero, GF2.zero, GF2.zero, GF2.one, GF2.one, GF2.zero],
    'f': [GF2.zero, GF2.zero, GF2.zero, GF2.zero, GF2.zero, GF2.one, GF2.one]
}

def match_vector_sums_to(vector_dict, v):
    return set(
        vector.flatten2(
            [ x
              for x in vector.permutations_unordered_no_repeat(list(vector_dict))
              if vector.add(vector_dict[x[0]], vector_dict[x[1]]) == v
            ]
        )
    )

u0 = [GF2.zero, GF2.zero, GF2.one, GF2.zero, GF2.zero, GF2.one, GF2.zero]
u_0010010 = match_vector_sums_to(p4_vectors, u0)

u1 = [GF2.zero, GF2.one, GF2.zero, GF2.zero, GF2.zero, GF2.one, GF2.zero]
u_0100010 = match_vector_sums_to(p4_vectors, u1)

## 5: (Problem 5) GF2 Vector Addition B
# Use the same format as the previous problem

p5_vectors = {
    'a': [GF2.one, GF2.one, GF2.one, GF2.zero, GF2.zero, GF2.zero, GF2.zero],
    'b': [GF2.zero, GF2.one, GF2.one, GF2.one, GF2.zero, GF2.zero, GF2.zero],
    'c': [GF2.zero, GF2.zero, GF2.one, GF2.one, GF2.one, GF2.zero, GF2.zero],
    'd': [GF2.zero, GF2.zero, GF2.zero, GF2.one, GF2.one, GF2.one, GF2.zero],
    'e': [GF2.zero, GF2.zero, GF2.zero, GF2.zero, GF2.one, GF2.one, GF2.one],
    'f': [GF2.zero, GF2.zero, GF2.zero, GF2.zero, GF2.zero, GF2.one, GF2.one]
}

v0 = [GF2.zero, GF2.zero, GF2.one, GF2.zero, GF2.zero, GF2.one, GF2.zero]
v_0010010 = match_vector_sums_to(p5_vectors, v0)
p5_v1 = [GF2.zero, GF2.one, GF2.zero, GF2.zero, GF2.zero, GF2.one, GF2.zero]
v_0100010 = match_vector_sums_to(p5_vectors, p5_v1)

## 6: (Problem 6) Solving Linear Equations over GF(2)
#You should be able to solve this without using a computer.
x_gf2 = None

## 7: (Problem 7) Formulating Equations using Dot-Product
#Please provide each answer as a list of numbers
v1 = None
v2 = None
v3 = None

## 8: (Problem 8) Practice with Dot-Product
uv_a = None
uv_b = None
uv_c = None
uv_d = None

