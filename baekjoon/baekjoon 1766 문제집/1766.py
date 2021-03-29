import heapq
n, m = map(int, input().split())

problem = [[] for i in range(n + 1)]
pre = [0 for _ in range(n+1)]
heap, result = [], []

for _ in range(m):
    a, b = map(int, input().split())
    problem[a].append(b)
    pre[b] += 1

for i in range(1, n+1):
    if pre[i] == 0:
        heapq.heappush(heap, i)


while heap:
    num = heapq.heappop(heap)
    result.append(num)
    for i in problem[num]:
        pre[i] -= 1
        if pre[i] == 0:
            heapq.heappush(heap, i)

for i in result:
    print(i, end=' ')
