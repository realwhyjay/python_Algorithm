num = int(input())
num_list = []

for _ in range(num):
    num_list.append(int(input()))

num_list.sort()

for i in num_list:
    if i == i+1:
        continue
    print(i)
