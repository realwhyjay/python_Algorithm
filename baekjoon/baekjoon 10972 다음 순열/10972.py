num = int(input())
a = list(map(int, input().split()))


def next_permutations(a):
    i = len(a)-1
    # 끝에서부터 원소를 비교해주는데,
    # 앞의 원소가 뒤의 원소보다 크다면 해당 원소의 값을 저장한다
    while i > 0 and a[i-1] >= a[i]:
        i -= 1
    if i <= 0:
        # 만일 end가 0이라면 완벽한 내림차순이기 때문에 False를 리턴 해준다.
        return False

    # a[i-1] 뒤의 값중 제일 a[i-1]보다 큰 값중 제일 작은 값을 확인하고
    # 자리를 바꿔준다.
    j = len(a)-1
    while a[i-1] >= a[j]:
        j -= 1
    a[i-1], a[j] = a[j], a[i-1]

    # a[i-1]뒤의 값은 내림차순으로 정렬되어 있기 떄문에 뒤집어준다.
    j = len(a)-1
    while i < j:
        a[i], a[j] = a[j], a[i]
        i += 1
        j -= 1

    return True


if next_permutations(a):
    print(' '.join(map(str, a)))
else:
    print(-1)
