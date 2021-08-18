def GCD(a, b):
    if a < b:
        a, b = b, a
    if b == 0:
        return a
    else:
        return GCD(b, a % b)


t = int(input())

while t != 0:
    n = list(map(int, input().split()))
    sum = 0

    if n[0] != len(n)-1:
        break

    for i in range(1, len(n)-1):
        for j in range(i+1, len(n)):
            sum += GCD(n[i], n[j])
    print(sum)
    t -= 1
