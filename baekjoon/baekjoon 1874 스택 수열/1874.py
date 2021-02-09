num = int(input())
stack = []
result = []
count = 1
temp = True

for i in range(num):
    check = int(input())
    while count <= check:
        stack.append(count)
        result.append('+')
        count += 1
    if stack[-1] == check:
        stack.pop()
        result.append('-')
    else:
        temp = False

if temp == False:
    print("NO")
else:
    for i in result:
        print(i)
