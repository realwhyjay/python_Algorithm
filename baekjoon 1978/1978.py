case_num = int(input())
num_list = list(map(int, input().split()))
ans = 0

if case_num == len(num_list):
    for i in num_list:
        count = 0
        for j in range(1, i+1):
            if i % j == 0:
                count += 1
        if count == 2:
            ans += 1

print(ans)
