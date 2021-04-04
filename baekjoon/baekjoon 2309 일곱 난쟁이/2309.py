import sys

dwarf = []
for _ in range(9):
    dwarf.append(int(sys.stdin.readline()))


sum = sum(dwarf)

for i in range(9):
    for q in range(i+1, 9):
        if (sum-(dwarf[i]+dwarf[q]) == 100):
            fake1 = dwarf[i]
            fake2 = dwarf[q]
            dwarf.remove(fake1)
            dwarf.remove(fake2)
            break
    if(len(dwarf) != 9):
        break


dwarf.sort()
for i in dwarf:
    print(i)
