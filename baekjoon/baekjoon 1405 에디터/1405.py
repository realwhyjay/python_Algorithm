str = list(input())
curser = len(str)

for _ in range(int(input())):
    inst = list(input().split())
    if inst[0] == 'P':
        str.insert(curser+1, inst[1])

    elif inst[0] == 'L':
        if curser > 0:
            curser -= 1

    elif inst[0] == 'D':
        if curser != len(str)+1:
            curser += 1

    else:
        if curser >= 0:
            if curser == len(str):
                str.pop(-1)
                curser -= 1
            else:
                str.pop(curser)
                curser -= 1
for i in str:
    print(i, end='')
