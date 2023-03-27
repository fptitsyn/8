from itertools import *
s = "АМФИБРАХИЙ"
a = ["".join(x) for x in set(permutations(s))]
a = [x for x in a if any(x[i] in "АИ" and x[i + 1] in "АИ" for i in range(len(x) - 1))]
print(len(a))