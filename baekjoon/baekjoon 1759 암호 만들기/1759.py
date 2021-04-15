from itertools import combinations

l, c = map(int, input().split())
character = list(input().split())
pw = list(map(''.join, combinations(sorted(character), l)))
vowel = ['a', 'e', 'i', 'o', 'u']
result = []
pw.sort()

for i in pw:
    mo, ja = 0, 0
    for j in i:
        if j in vowel:
            mo += 1
        else:
            ja += 1
    if mo >= 1 and ja >= 2:
        result.append(i)

for t in result:
    for k in t:
        print(k, end='')
    print()
