T = int(input())

for _ in range(T):
    N = int(input())
    result = 0
    for i in range((N//3)+1):
        for j in range((N//2)+1):
            for k in range(N+1):
                if ((3*i)+(2*j)+k) == N:
                    result += 1
                    print(f'3: {i}    2 : {j}    1 : {k}')
    print(result)
