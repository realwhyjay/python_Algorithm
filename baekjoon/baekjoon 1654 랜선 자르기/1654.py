k, n = map(int, input().split())
lan = []

for _ in range(k):
    lan.append(int(input()))

# 이분 탐색을 하기 위해 오름차순으로 정렬해준다.
lan.sort()

# 가장 작은 수인 1부터 시작해서
start = 1
# 정렬된 값중 가장 큰 수 까지를 범위로 잡는다.
end = lan[-1]

# 이분 탐색이 끝날 때까지 while문을 돌린다.
while start <= end:
    mid = (start+end)//2  # 중간 위치
    lines = 0  # 랜선의 수

    for i in lan:
        lines += (i // mid)  # 분할 된 랜선의 수를 체크한다.

    # 분할된 랜선의 개수를 기준으로 탐색을 진행한다.
    if lines >= n:
        # 분할된 총 랜선의 수가 N보다 많다면, 원하는 값보다 더 작게 나누어준 것이니까
        # start 값을 mid+1 로 더 크게 만들어준다.
        start = mid + 1
    else:
        # 분할된 총 랜선의 수가 N보다 작다면, 원하는 값보다 더 크게 나누어준 것이니까
        # end 값을 mid-1 로 더 작게 만들어준다.
        end = mid - 1

print(start)
