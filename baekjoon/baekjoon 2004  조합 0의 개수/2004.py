n, m = map(int, input().split())
# 조합 공식 n!/(n-m)!m!
# 이거 그대로 구현하면 메모리 개박살!
# 0의 개수는 10을 몇번이나 곱해주느냐와 같은 말이기 때문에
# n,m이 가지고 있는 2 또는 5의 개수중 작은 수가 10의 개수라고 할 수 있다.

# 해당함수는 i!가 가지고 있는 j의 개수를 구해주는 함수이다.
# 근데 나 응애 문레기 왜 이거 이렇게 코드가 짜여있는지 이해가 안된다
# 예를들어 10!에서 2의 개수를 구할때
# 10을 2로 나눈 몫을 계속 2로 나누어져 더이상 나누어질 때까지 나누고
# 그 몫을 더해준 것이 10!에 있는 2의 개수인데 이게 어떻게 가능한거지
# 왜 그 몫들을 더해준건이 2의 개수가 될 수 있는건지 이해가 안된다... ㅜ


def count_number(i, j):
    count = 0
    while i:
        i //= j
        count += i
    return count


two_count = count_number(n, 2)-count_number(m, 2)-count_number(n-m, 2)
five_count = count_number(n, 5)-count_number(m, 5)-count_number(n-m, 5)
print(min(two_count, five_count))
