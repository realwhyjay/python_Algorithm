string = list(input())
n = [-1]*26

for i in range(len(string)):
    if (n[ord(string[i])-ord('a')] == -1):
        n[ord(string[i])-ord('a')] = i

for i in n:
    print(i, end=' ')
