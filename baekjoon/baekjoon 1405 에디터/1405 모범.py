import sys

str1 = list(sys.stdin.readline().strip())
str2 = []

for _ in range(int(input())):
    inst = list(sys.stdin.readline().strip())
    if inst[0] == 'P':
        str1.append(inst[2])
    elif inst[0] == 'L' and str1 != []:
        str2.append(str1.pop())
    elif inst[0] == 'D' and str2 != []:
        str1.append(str2.pop())
    elif inst[0] == 'B' and str1 != []:
        str1.pop()

print("".join(str1 + list(reversed(str2))))
