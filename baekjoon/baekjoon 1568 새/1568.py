print("들어왔냐1")
N = int(input())
print("들어왔냐")
print(N)

K = 1
count = 0

while N > 0:
    if N < K:
        K = 1
        print("N보다 K가 클 때")
    else:
        N -= K
        print("지금 N : {} K : {}".format(N, K))
        K += 1
        count += 1
        print("지금 count : {}".format(count))

print(count)
