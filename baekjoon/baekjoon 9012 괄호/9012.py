T = int(input())

for _ in range(T):
    check = 0
    list = input()
    for i in list:
        if i == '(':
            check += 1
        else:
            check -= 1
            if check < 0:
                break

    if check == 0:
        print("YES")
    else:
        print("NO")
