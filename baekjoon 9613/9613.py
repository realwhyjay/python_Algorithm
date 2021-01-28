n = int(input())


def GCD(a, b):
    if b == 0:
        return a
    else:
        return GCD(b, a % b)


for k in range(n):
    num_list = list(map(int, input().split()))
    num_count = len(num_list)
    sum = 0

    for i in range(1, num_count-1):
        for j in range(i+1, num_count):
            sum += GCD(num_list[i], num_list[j])

    print(sum)
