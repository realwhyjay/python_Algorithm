import random

n = int(input('난수 입력 : '))

for _ in range(n):
    r = random.randint(10, 99)
    print(r, end=' ')
    if r == 13:
        print('\n 프로그램을 중단합니다')
        break
else:
    print('\n 난수 생성을 종료합니다.')
