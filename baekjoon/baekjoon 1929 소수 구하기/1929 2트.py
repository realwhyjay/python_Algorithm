M, N = map(int, input().split())

check = [True]*(N+1)

for i in range(2, int((N+1)**0.5)+1):
    if check[i] == True:
        for j in range(2*i, N+1, i):
            check[j] = False

for k in range(M, N+1):
    if k > 1 and check[k] == True:
        print(k)
