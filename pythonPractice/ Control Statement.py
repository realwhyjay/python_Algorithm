
# if문
weather = input("오늘 날씨는 어때요? ")
if weather == "비" or "눈":
    print("우산을 챙기세요")
elif weather == "미세먼지":
    print("마스크를 챙기세요")
else:
    print("준비될 필요 없어요")

temp = int(input("기온은 어때요? "))
if 30 <= temp:
    print("너무 더워요 나가지 마세요")
elif 10 <= temp and temp < 30:
    print("괜찮은 날씨에요")
elif 0 <= temp < 10:
    print("외투를 챙기세요")
else:
    print("너무 추워요. 나가지 마세요")


# for문
for waiting_no in [0, 1, 2, 3, 4]:
    print("대기번호 : {0}".format(waiting_no))

for waiting_no in range(5):
    print("대기번호 : {0}".format(waiting_no))

for waiting_no in range(1, 6):  # 1부터 6전까지
    print("대기번호 : {0}".format(waiting_no))

starbucks = ["아이언맨", "토르", "아이엠 그루트"]
for customer in starbucks:  # 스타벅스라는 리스트에 있는 사람들 한명한명을 출력하는 것
    print("{0}, 커피가 준비되었습니다.".format(customer))


# while문
customer = "토르"
index = 5
while index >= 1:
    print("{0}, 커피가 준비되었습니다. {1}번 남았어요".format(customer, index))
    index -= 1
    if index == 0:
        print("커피는 폐기처분되었습니다")


customer = "토르"
person = "Unknown"

while person != customer:
    print("{0}, 커피가 준비되었습니다.".format(customer))
    person = input("이름이 어떻게 되세요? ")
print("토르가 커피를 받아갔다!")


# continue와 break
# continue는 이어지는 명령을 실행시키지 않고 그 다음 반복문을 진행시키도록 하는 것
absent = [2, 5]
no_book = [7]
for student in range(1, 11):
    if student in absent:
        continue
    elif student in no_book:
        print("오늘 수업 여기까지. {0}는 교무실로 따라와" .format(student))
        break
    print("{0}, 책을 읽어봐" .format(student))


# 한줄 for
# 출석번호가 1 2 3 4, 앞에 100을 붙이기로 함 -> 101, 102, 103, 104.
students = [1, 2, 3, 4, 5]
print(students)

students = [i+100 for i in students]
# students라는 list에 있는 요소들을 i로 하나씩 불러 오고, 거기에 100을 더한 값을 리스트로 바꾸어 집어넣으라는 의미
print(students)

# 학생 이름을 길이로 변환
students = ["아이언맨", "토르", "그루트"]
print(students)
students = [len(i) for i in students]
print(students)

# 학생 이름을 대문자로 변환
students = ["Iron man", "Thor", "Groot"]
print(students)
students = [i.upper() for i in students]
print(students)
