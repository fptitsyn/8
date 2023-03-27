from itertools import *
s = "soika"
a = ["".join(x) for x in set(product(s, repeat=5))]
a = sorted(a)
for i in range(len(a) - 1, -1, -1):
    if "ss" not in a[i] and a[i].count("o") <= 1:
        print(i + 1)
        break
