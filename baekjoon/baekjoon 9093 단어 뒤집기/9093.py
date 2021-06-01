T = int(input())

for _ in range(T):
    word = list(map(list, input().split()))
    for i in word:
        for j in reversed(i):
            print(j, end='')
        print(' ', end='')
    print()
