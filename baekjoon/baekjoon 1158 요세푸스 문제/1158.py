N, K = map(int, input().split())

list = [i for i in range(1, N+1)]
result = []
next = 0

for i in range(N):
    next += K-1
    if next >= len(list):
        next %= len(list)

    result.append(str(list.pop(next)))

print("<", ", ".join(result)[:], ">", sep='')
