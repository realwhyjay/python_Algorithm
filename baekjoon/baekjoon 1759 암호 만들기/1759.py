from itertools import combinations

l, c = map(int, input().split())
character = list(input().split())
pw = list(combinations(sorted(character), 4))
vowel = ['a', 'e', 'o', 'i', 'u']
result = []
mo, ja = 0, 0
pw.sort()

for i in pw:
    for j in i:
        if j in vowel:
            mo += 1
        else:
            ja += 1
    if mo >= 1 and ja >= 2:
        result.append(i)

for i in pw:
    for j in i:
        print(j, end='')
    print()
