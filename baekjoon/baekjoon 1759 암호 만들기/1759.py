from itertools import combinations


l, c = map(int, input().split())
character = list(input().split())
pw = list(combinations(sorted(character), 4))

for i in pw:
    for j in i:
        print(j, end='')
    print()
