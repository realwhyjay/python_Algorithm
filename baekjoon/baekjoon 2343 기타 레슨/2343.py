N, M = map(int, input().split())
lesson = list(map(int, input().split()))

start = 1
end = max(lesson)

while start <= end:
    mid = (start + end)//2
    time = 0
    count = 0

    for i in lesson:
        if i >= mid:
            time = 0
            count += 1
        time += i

    if count > M:
