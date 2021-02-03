from random import *
from math import *  # math 라이브러리안에 있는 모든 것을 이용하겠다는 의미
print(5)
print(-10)
print(3.14)
print(123124125)
print(5+8)
print(8/3)
print(8 % 3)

print("풍선")
print('풍풍선')
print("v"*9)


print(5 > 10)
print(5 < 10)
print(True)
print(False)
print(not True)


# 애완동물을 소개해 주세요~
animal = "강아지"
name = "연탄이"
age = 4
hobby = "산책"
is_adult = age >= 3

print("우리집" + animal + "의 이름은" + name + "에요")
print(name + "는 " + str(age) + "살이며, 산택을 아주 좋아해요")
print(name + "는 어른일까요?" + str(is_adult))

print(2**3)  # 2의 3승
print(5 % 3)  # 나머지


# 간단한 수식
number = 2+3*4
print(number)

number = number+2
print(number)

number += 2
print(number)
number -= 2
print(number)
number *= 2
print(number)
number /= 2
print(number)
number %= 2
print(number)


# 숫자 처리 함수
print(abs(-5))  # 절대값
print(pow(4, 2))  # 4^2 = 16. 제곱이 나옴
print(max(5, 12))  # 최대값
print(min(5, 12))  # 최소값
print(round(3.14))  # 반올림
print(round(4.99))

# math 라이브러리 사용하는 것
print(floor(4.99))  # 내림,4
print(ceil(3.19))  # 올림,4
print(sqrt(16))  # 제곱근을 구하는 것,4


# 랜덤함수(난수)

print(random())  # 0.0이상 1.0 미만의 임의의 값을 생성하는 것.
print(random() * 10)  # 0.0이상 10.0 미만의 임의의 값을 생성하는 것.
print(int(random() * 10))  # 0 이상 10 미만의 임의의 값을 생성하는 것.

print(int(random() * 10) + 1)  # 1 이상 10 이하의 임의의 값을 생성하는 것.

# 로또 값 출력해보자
print(int(random()*45)+1)  # 1~45 의 임의의 값 생성

# 이걸 더 쉽게 작성하는 방법
print(randrange(1, 45))  # 1~45 미만의 임의의 값 생성
print(randrange(1, 46))  # 1~45의 임의의 값 생성

print(randint(1, 45))  # randint는 저 두 값을 모두 포함하는 임의의 값 생성하는 것


# 문자열
sentence = '나는 소년입니다'
print(sentence)

sentence2 = "파이썬은 쉬워요"
print(sentence2)

sentence3 = """
나는 소년입니다.
파이썬은 쉬워요
정말입니다.
"""
print(sentence3)


# 슬라이싱
jumin = "940420-1069210"
print("성별 : " + jumin[7])
print("연 : " + jumin[0:2])  # :을 사용해서 0번째부터 2번째 직전 값까지 가져오는 것
print("월 : " + jumin[2:4])  # :을 사용해서 2번째부터 4번째 직전 값까지 가져오는 것
print("월 : " + jumin[4:6])  # :을 사용해서 4번째부터 6번째 직전 값까지 가져오는 것


print("생년월일 : " + jumin[0:6])  # 처음부터 가져오는거니까 0을 지워도 된다.
print("뒤 7자리 : " + jumin[0:14])  # 끝까지 가져오는거니까 14를 지워도 된다.
print("뒤 7자리 (뒤에부터) : " + jumin[-7:])  # 맨 뒤 7번째부터 끝까지


# 문자열 처리 함수
python = "Python is Amazing"
print(python.lower())  # 소문자로 출력
print(python.upper())  # 대문자로 출력
print(python[0].isupper())  # 0번째 문자가 대문자인지 파악
print(len(python))  # 전체 길이 반환
# python을 swift로 바꿔서 출력한다. 변수 내용은 바뀐거 아니고 출력만 바꿔서 해주는 것
print(python.replace("Python", "Swift"))

index = python.index("n")  # index를 사용하면 어떤 문자가 어디에 있는지를 알 수 있다.
print(index)

index = python.index("n", index + 1)
# 그 이후에도 더 있는지 찾는다. 뒤에는 어디부터 찾을지를 정해주는 것.
# 원하는 값이 없을 때는 프로그램을 종료해버린다.
print(index)

print(python.find("Swift"))  # index랑 비슷하게 원하는 문자가 어디에 포함되어있는지 위치를 반환
# 근데 지금 Swift라는게 없으니까 반환값은 -1이 된다. 반환값이 있다는 점에서 index와 차이를 가진다

print(python.count("n"))  # 찾는 문자가 몇개나 있는지 세어주는 것


# 문자열 포맷
print("a"+"b")
print("a", "b")

# 출력 방법 1
print("나는 %d살입니다" % 20)  # 정수
print("나는 %s을 좋아해요." % "파이썬")  # 문자열
print("Apple은 %c로 시작해요" % "A")  # 문자
# %s로만 쓰면 정수건 하나의 문자건 상관없이 다 출력이 가능하다.

print("나는 %s색과 %s색을 좋아해요." % ("파란", "빨간"))

# 출력 방법 2 중괄호 사용
print("나는 {}살입니다".format(20))
print("나는 {}색과 {}색을 좋아해요." .format("파란", "빨간"))
# 순서를 임의로 정할수도 있음
print("나는 {0}색과 {1}색을 좋아해요." .format("파란", "빨간"))
print("나는 {1}색과 {0}색을 좋아해요." .format("파란", "빨간"))

print("나는 {0}색과 {1}색을 좋아해요." .format("파란", "빨간"))

# 출력 방법 3 - 이 경우에는 순서와 상관없이 출력이 가능하다.
print("나는 {age}살이며 {color}색을 좋아해요." .format(age=20, color="빨간"))
print("나는 {age}살이며 {color}색을 좋아해요." .format(color="빨간", age=20))

# 출력 방법 4 - 변수를 사용
age = 20
color = "빨간"
print(f"나는 {age}살이며, {color}색을 좋아해요.")
