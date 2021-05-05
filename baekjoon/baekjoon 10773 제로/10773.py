import sys

k = int(input())
money = []
for _ in range(k):
    num = int(sys.stdin.readline())
    if num == 0:
        money.pop()
    else:
        money.append(num)

print(sum(money))
