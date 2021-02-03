# 함수
# 함수 선언
def open_account():
    print("새로운 계좌가 생성되었습니다.")


# 함수 호출
open_account()


# 전달값과 반환값
def deposit(balance, money):  # 입금
    print("입금이 완료되었습니다. 잔액은 {} 원 입니다.".format(balance + money))
    return balance + money


def withdraw(balance, money):  # 출금
    if balance >= money:  # 잔액이 출금보다 많으면
        print("출금이 완료되었습니다. 잔액은 {} 원 입니다.".format(balance - money))
        return balance - money
    else:
        print("출금이 완료되지 않았습니다. 잔액은 {} 원 입니다.".format(balance))
        return balance


def withdraw_night(balance, money):  # 저녁에 출금
    commission = 100  # 수수로 100원
    return commission, balance - money - commission  # 두개의 값을 ,로 구분해서 반환해준다


balance = 0
balance = deposit(balance, 1000)
balance = withdraw(balance, 2000)
balance = withdraw(balance, 500)
balance = deposit(balance, 1000)


commission, balance = withdraw_night(balance, 500)
print("수수료는 {} 원이며, 잔액은 {} 원입니다.".format(commission, balance))


# 기본값
def profile(name, age, main_lang):
    print("이름 : {} \t나이 : {}\t주 사용 언어 : {}"
          .format(name, age, main_lang))


profile("유재석", 20, "파이썬")
profile("김태호", 25, "자바")

# 만약 매번 같은 값이 들어가는 경우라면? --> 그 때 사용하는 것이 기본값
# 함수 호출 시 전달받은 값이 없을때 사용하는 것이 기본값이다.


def profile2(name, age=17, main_lang="파이썬"):
    print("이름 : {} \t나이 : {}\t주 사용 언어 : {}"
          .format(name, age, main_lang))


profile2("최영재")
profile2("버디")
profile2("김태호", 27, "자바")


# 키워드 값
# 키워드를 이용해서 값을 지정해주면, 순서 상관없이 값을 입력하여 함수호출이 가능하다
def profile3(name, age, main_lang):
    print(name, age, main_lang)


profile3(name="최버디", main_lang="파이썬", age=17)
profile3(main_lang="Swift", age=20, name="최영재")


# 가변인자
def profile4(name, age, lang1, lang2, lang3, lang4, lang5):
    # end = " "  이걸 적으면 프린트문이 끝나고 줄바꿈을 하지 않은채 이어서 다음 문장을 출력하게 된다.
    print("이름 : {}\t나이 : {}\t".format(name, age), end=" ")
    print(lang1, lang2, lang3, lang4, lang5)


profile4("최영재", 20, "python", "java", "cpp", "swift", "js")
profile4("최버디", 20, "kotlin", "java", "", "", "")

# 만약 언어를 다섯개보다 적게 알거나, 다섯개 넘게 알고 있는 사람이 있다면???
# 이때 사용할 수 있는게 가변인자이다.


def profile5(name, age, *language):
    print("이름 : {}\t나이 : {}\t".format(name, age), end=" ")
    for lang in language:
        print(lang, end=" ")
    print()


profile5("최영재", 20, "python", "java", "cpp", "swift", "js", "kotlin")
profile5("최버디", 20, "kotlin", "java")
# 다른 개수의 값이 있지만, 하나의 함수를 쓸 수 있다.
