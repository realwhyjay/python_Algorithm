def pactorial(N):
    if N == 0 or N == 1:
        return 1
    return N*pactorial(N-1)


N = int(input())

result = list(str(pactorial(N)))
count = 0

for i in range(len(result)-1, 0, -1):
    if result[i] == "0":
        count += 1
    else:
        break

print(count)
