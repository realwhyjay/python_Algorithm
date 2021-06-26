n = int(input())

length = len(str(n))

ans = 0
# 1의 자리일 때는,  한자리 수가 1~9 까지
# 10의 자리일 때는, 두자리를 차지하는 수가 10~99 까지
# 100의 자리일 때는, 세 자리를 차지하는 수가 100~999까지 ......
for i in range(1, length):
    ans += i * (pow(10, i) - pow(10, i - 1))

# 입력받은 수의 최대 자리수의 경우에는, 해당수가 차지하는 자리수 만큼만 계산해서 더해준다.
ans += length * (n - pow(10, length - 1) + 1)
print(ans)
