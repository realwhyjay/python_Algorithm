import heapq
import sys

n = int(input())
card = []
result = 0
for _ in range(n):
    heapq.heappush(card, int(sys.stdin.readline()))

while(len(card) != 1):
    x = heapq.heappop(card)
    y = heapq.heappop(card)
    heapq.heappush(card, x+y)
    result += (x+y)
print(result)
