string = list(input())
n = [0]*26

for i in range(len(string)):
    n[ord(string[i])-ord('a')] += 1

for i in n:
    print(i, end=' ')
