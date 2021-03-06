N = int(input())

K = 1
count = 0

while N > 0:
    if N < K:
        K = 1
    else:
        N -= K
        K += 1
        count += 1

print(count)
