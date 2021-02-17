N = int(input())
Nlist = list(map(int, input().split()))
M = int(input())
Mlist = list(map(int, input().split()))

for i in range(len(Mlist)):
    print(1) if Nlist.count(Mlist[i]) >= 1 else print(0)
