from itertools import product

n, m = map(int, input().split())
num = [i for i in range(1, n+1)]

result = list(product(sorted(num), repeat=m))

for k in sorted(result):
    for j in k:
        print(j, end=' ')
    print()
