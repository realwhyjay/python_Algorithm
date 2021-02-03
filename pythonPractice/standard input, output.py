# 표준 입출력
# sep을 사용하면 각 요소들 사이를 원하는 문자열로 구분지어줄 수 있다.
import pickle
import sys
print("python", "java", "swift", sep=" vs ")

# end를 사용하면 문장의 끝부분을 정할 수 있다.
# 문장은 기본적으로 줄넘김을 하도록 되어있는데, end를 사용하면 그 줄바꿈을 해당 문자열로 바꿀 수가 있는 것.
print("버디", "최영재", "swift", sep=",", end="?")
print("무엇이 더 재밌을까요?")

# sys를 import한 뒤 stdout을 해주면 표준 출력으로 문장을 print 하는 것이고
# stderr을 해주면 표준 에러로 처리가 된다.

print("Python", "Swift", file=sys.stdout)
#print("Python", "Swift", file=sys.stderr)

# 좌우 정렬하기
scores = {"수학": 0, "영어": 50, "코딩": 100}
for subject, score in scores.items():
    # ljust = 왼쪽으로 정렬을 하는데 8칸만큼의 공간을 확보하는 것.
    # 현재 예시에서 과목 이름은 8칸을 확보해서 왼쪽정렬, 점수는 4칸을 확보하여 오른쪽 정렬을 해준 것.
    print(subject.ljust(8), str(score).rjust(4), sep=":")


# zfill() = 지정한 숫자만큼 공간을 확보하여 출력을 해주는데, 값이 없는 빈공간은 0으로 채워주는 것.
for num in range(1, 21):
    print("대기번호 : " + str(num).zfill(3))
# 실제값은 1,2,3 인데 0을 붙여서 출력되는걸 확인할 수가 있다.


# 표준 입력
# input()안에 있는 문장을 출력하고 나서 사용자로부터 값을 입력받는다.
answer = input("아무 값이나 입력하세요 : ")
print(type(answer))
print("입력하신 값은 " + answer + "입니다.")

# input을 해서 값을 입력받으면 항상 string으로 값이 저장된다.


# 다양한 출력 포맷
# 빈 자리는 빈공간으로 두고, 오른쪽 정렬을 하되, 총 10자리 공간을 확보
print("{0: >10}".format(500))
# 양수 일때는 +로 표시, 음수일 땐 -로 표시
print("{0: >+10}".format(500))
print("{0: >+10}".format(-500))

# 왼쪽 정렬하고, 빈칸을 _로 채움
print("{0:_<+10}".format(500))
# 3자리 마다 콤마를 찍어주기
print("{0:,}".format(100000000000000))
# 3자리 마다 콤마를 찍어주기, +- 부호도 붙이기
print("{0:+,}".format(100000000000000))
print("{0:+,}".format(-100000000000000))

# 3자리 마다 콤마르 찍어주기, 부호도 붙이고, 자릿수 확보하기, 빈자리는 ^로 채워주기
print("{0:^<+30,}".format(100000000000000))

# 소수점 출력
print("{0:f}".format(5/3))
# 소수점 특정 자리수 까지만 표시(예시의 경우에는 소수점 3번째 자리에서 반올림)
print("{0:.2f}".format(5/3))


# 파일 입출력
# w를 쓰는 경우에는 쓰기모드. 덮어쓰기만 가능하다.
score_file = open("score.txt", "w", encoding="utf8")
print("수학 : 0", file=score_file)
print("영어 : 50", file=score_file)
score_file.close()

# a를 쓰는 경우에는 뒤에서 이어써 쓸 수 있다. append의 의미.
score_file = open("score.txt", "a", encoding="utf8")
score_file.write("과학:80")
score_file.write("\n코딩:100")
# 위에서 프린트를 했던 경우에는 알아서 줄넘김이 되지만, write를 해주는 경우에는 줄변경을 직접 해주어야한다.
score_file.close()


# r를 쓰는 경우에는 읽기모드이다.
score_file = open("score.txt", "r", encoding="utf8")
# 아래의 코드로는 파일의 모든 내용을 출력해준다.
print(score_file.read())
score_file.close()

# 파일 전체가 아니라 한 줄씩 출력을 원할때는?
score_file = open("score.txt", "r", encoding="utf8")
# 아래의 코드로는 줄 별로 내용을 읽어준다. 한 줄 읽고 커서는 다음 줄로 이동한다
print(score_file.readline())
print(score_file.readline())
# print로 출력하기 때문에 줄바꿈이 일어나는데, 그걸 원치 않을 때는 다음과 같이 작성해주면 된다.
print(score_file.readline(), end="")
print(score_file.readline())
score_file.close()


# 만약 다른 사람이 가져온 파일이 몇 줄 짜리인지 모르는 경우라면?
score_file = open("score.txt", "r", encoding="utf8")
while True:
    line = score_file.readline()
    if not line:
        break
    print(line, end="")
score_file.close()


# 리스트 형식으로 처리할 수도 있다.
score_file = open("score.txt", "r", encoding="utf8")
lines = score_file.readlines()  # 모든 라인을 list 형태로 저장
for line in lines:
    print(line)
score_file.close()


# pickle - 프로그램에서 우리가 사용하는 데이터를 파일 형태로 저장해주는 것.
# wb는 쓰기모드인데 b는 바이너리 타입을 의미한다.
profile_file = open("profile.pickle", "wb")
profile = {"이름": "최영재", "나이": 28, "취미": ["게임", "코딩", "영화"]}
print(profile)
# 피클을 이용해서 위의 데이터를 파일에다 쓰려면, dump를 사용해야함
pickle.dump(profile, profile_file)
# profile에 있는 정보를 profile_file에 저장
profile_file.close()

# pickle의 파일을 가져오기
# wb 대신 rb를 해줌
profile_file = open("profile.pickle", "rb")
profile = pickle.load(profile_file)  # profile_file에 있는 정보를 profile에 불러오기
print(profile)
print("파일에서 불러온거임")
profile_file.close()


# with
# with를 쓰면 더 편하게 파일을 열고, 처리하고 닫는 과정을 처리할 수 있다.


# 이렇게하면 close 할 필요없이 처리가 가능하다.
with open("profile.pickle", "rb") as profile_file:
    print(pickle.load(profile_file))


# 새로운 파일을 만들고 불러오기
with open("study.txt", "w", encoding="utf8") as study_file:
    study_file.write("파이썬을 열심히 공부하고 있어요.")

with open("study.txt", "r", encoding="utf8") as study_file:
    print(study_file.read())
