from itertools import permutations

n, m = map(int, input().split())
num = list(map(int, input().split()))

result = list(permutations(sorted(num), m))

for k in result:
    for j in k:
        print(j, end=' ')
    print()
