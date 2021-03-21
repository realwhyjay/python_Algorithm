N, M = map(int, input().split())
lesson = list(map(int, input().split()))

start = 1
end = sum(lesson)

while start <= end:
    mid = (start + end)//2
    time = 0
    count = 1

    for i in lesson:
        time += i
        if time > mid:
            count += 1
            time = i

    if count > M:
        start = mid+1
    else:
        end = mid-1

print(start)
