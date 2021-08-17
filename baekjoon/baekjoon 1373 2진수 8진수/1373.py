before = input()
number = []
last = len(before)
result = []
for i in range(len(before)-1, -1, -3):
    if i == len(before)-1:
        continue
    else:
        number.append(before[i+1:last])
        last = i+1
number.append(before[:last])

for i in reversed(number):
    temp = 0
    for j in range(len(i)):
        temp += int(i[j]) * 2 ** (len(i)-1-j)
    result.append(str(temp))

print(int(''.join(result)))
