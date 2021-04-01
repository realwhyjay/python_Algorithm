import heapq
n, m = map(int, input().split())

problem = [[] for i in range(n + 1)]
pre = [0 for _ in range(n+1)]
heap, result = [], []

for _ in range(m):
    a, b = map(int, input().split())
    problem[a].append(b)  # 연결된 간선. a번 문제는 b번보다 먼저 풀어야한다
    pre[b] += 1  # b번문제는 몇개의 선행문제와 연결되어있는지를 카운팅한다.

for i in range(1, n+1):
    if pre[i] == 0:  # 아무런 선행문제가 없는 경우
        heapq.heappush(heap, i)

while heap:
    num = heapq.heappop(heap)  # 선행문제가 없는 문제들 중 난이도가 낮은 것부터 꺼낸다
    result.append(num)
    for i in problem[num]:  # 해당 선행문제를 풀었을 때 풀 수 있는 문제들을 확인한다.
        pre[i] -= 1
        if pre[i] == 0:  # 더 이상 선행문제가 없으면 0이되고, 그러면 그 문제를 heap에 넣는다.
            heapq.heappush(heap, i)

for i in result:
    print(i, end=' ')
