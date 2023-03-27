from itertools import *

s = [1, 2, 5, 10]

a = []
for k in range(10, 101):
    a += [x for x in combinations_with_replacement(s, k) if sum(x) == 100]

print(len(a))