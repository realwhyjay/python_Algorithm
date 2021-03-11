n, m = map(int, input().split())

height = list(map(int, input().split()))


start = 1
end = max(height)


while start <= end:
    mid = (start+end)//2
    result = 0

    for i in height:
        if (i-mid) > 0:
            result += (i - mid)

    if result >= m:
        start = mid+1
    else:
        end = mid-1

print(end)
