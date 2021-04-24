def pactorial(N):
    if N == 0 or N == 1:
        return 1
    return N*pactorial(N-1)


N = int(input())

print(pactorial(N))
