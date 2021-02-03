# 리스트 []
subway = [10, 20, 30]
print(subway)

subway = ["유재석", "조세호", "박명수"]
print(subway)

# 조세호가 몇 번째 칸에 타고 있는가?
print(subway.index("조세호"))

# 하하가 다음 정류장에서 다음 칸에 탔다
subway.append("하하")
print(subway)

# 정형돈이 두번째 칸에 탔다
subway.insert(1, "정형돈")
print(subway)

# 맨 뒤에칸부터 한명씩 내린다면?
print(subway.pop())
print(subway)
print(subway.pop())
print(subway)
print(subway.pop())
print(subway)

# 같은 이름의 사람이 몇명 있는지 확인
subway = ["유재석", "조세호", "박명수", "하하"]
subway.append("유재석")
print(subway)
print(subway.count("유재석"))

# 리스트는 정렬도 가능
num_list = [5, 2, 3, 4, 1]
print(num_list)
num_list.sort()
print(num_list)

# 순서 뒤집기 가능
num_list.reverse()
print(num_list)

# 모두 지우기
num_list.clear()
print(num_list)

# 다양한 자료형 함께 사용 가능
mix_list = ["조세호", 20, True]
print(mix_list)

# 리스트 확장
num_list = [5, 2, 3, 4, 1]
num_list.extend(mix_list)
print(num_list)


# 딕셔너리 {key: value}로 구성. 키는 중복사용 불가능
cabinet = {3: "유재석", 100: "김태호"}
print(cabinet[3])
print(cabinet[100])

print(cabinet.get(3))
print(cabinet.get(100))

# 키가 없는데 대괄호를 사용하여 반환을 하려는 경우에는 프로그램이 종료된다
# print(cabinet[5])
# 반면 키가 없는데 get을 사용하려 반환하는 경우에는 None를 반환한다.

# 값이 없는 경우에는 원하는 값을 출력할수 있도록 할 수 있다.
print(cabinet.get(5, "사용 가능"))

# 사전 자료형 안에 어떤 값이 있는지 확인하는 방법
print(3 in cabinet)
print(5 in cabinet)
# key를 넣고 그게 cabinet에 있느냐를 물어보는 것

# key는 스트링 값도 사용이 가능하다.
cabinet = {"A-3": "유재석", "B-100": "김태호"}
print(cabinet["A-3"])
print(cabinet["B-100"])

# 새로운 값을 추가하는 경우
print(cabinet)
cabinet["C-20"] = "조세호"
cabinet["A-3"] = "최영재"
# 원래 있던 키에 값을 배정하는 경우에는 이전 값대신 새로운 값이 들어간다.
print(cabinet)

# 값을 삭제하는 경우
del cabinet["A-3"]
print(cabinet)

# key들만 출력하는 경우
print(cabinet.keys())

# value들만 출력하는 경우
print(cabinet.values())

# key, value를 쌍으로 출력하는 경우
print(cabinet.items())

# 딕셔너리를 지우는 경우
cabinet.clear()
print(cabinet)


# 튜플 - list와 다르게 내용 변경이나 추가를 할 수가 없다.
# 대신 속도가 빠르다는 장점이 있다.
menu = ("돈가스", "치즈가스")
print(menu[0])
print(menu[1])

# 어디서 활용하나?
name = "최영재"
age = 28
hobby = "코딩"
print(name, age, hobby)

# 튜플을 사용하면 한번에 선언이 가능하다
(name, age, hobby) = ("최영재", 28, "코딩")
print(name, age, hobby)


# 집합 (set)
# 중복이 안되고 순서가 없다.
my_set = {1, 2, 3, 3, 3}
print(my_set)

java = {"유재석", "김태호", "양세형"}
python = set(["유재석", "최영재"])

# 교집합 (java와 python을 모두 할 수 있는 개발자)
print(java & python)
print(java.intersection(python))

# 합집합 (java도 할 수 있거나 python도 할 수 있는 개발자)
print(java | python)
print(java.union(python))

# 차집합 (자바는 할 수 있지만 파이썬을 할 수 없는 개발자)
print(java-python)
print(java.difference(python))

# 집합에 추가 또는 삭제 가능
python.add("김태호")
print(python)

java.remove("김태호")
print(java)


# 자료구조의 변경
menu = {"커피", "우유", "쥬스"}
print(menu, type(menu))
# 현재는 set상태


# 타입을 리스트로 바꿀 수 있다
menu = list(menu)
print(menu, type(menu))

menu = tuple(menu)
print(menu, type(menu))

menu = set(menu)
print(menu, type(menu))
