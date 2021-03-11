n = int(input())
area = list(map(int, input().split()))
limit = int(input())

start = 1
end = max(area)

print("시작하자!! start : {} end : {} mid : {}".format(start, end, (start+end)//2))

while start <= end:
    mid = (start+end)//2
    result = 0

    for i in area:
        if i > mid:
            result += mid
        else:
            result += i

    if result > limit:
        end = mid - 1
    else:
        start = mid + 1
    print("start : {} end : {} mid : {} result : {}".format(
        start, end, mid, result))

print(end)
