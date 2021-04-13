from itertools import permutations

n = int(input())
lst = [i for i in range(1, n+1)]

for j in list(permutations(lst)):
    for k in j:
        print(k, end=' ')
    print()
