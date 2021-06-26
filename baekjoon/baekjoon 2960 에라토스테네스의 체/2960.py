N, K = map(int, input().split())
count = 0
nums = [True] * (N+1)

for i in range(2, len(nums)+1):
    for j in range(i, N+1, i):
        if nums[j] == True:
            nums[j] = False
            count += 1
        if count == K:
            print(j)
            break
