num = int(input())
num_list = [0 for i in range(num+1)]
num_list[1] = 1

for i in range(2, num+1):
    num_list[i] = num_list[i-1]+num_list[i-2]
    print(
        "i: {} [i-2] : {}  [i-1] : {}  [i] : {}".format(i, num_list[i-2], num_list[i-1], num_list[i]))

print(num_list[num])
