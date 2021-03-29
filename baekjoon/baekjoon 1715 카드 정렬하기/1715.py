import heapq
n = int(input())
card = []
result = 0
for _ in range(n):
    heapq.heappush(card, int(input()))

while(len(card) != 1):
    x = heapq.heappop(card)
    y = heapq.heappop(card)
    heapq.heappush(card, x+y)
    result += (x+y)
print(result)
