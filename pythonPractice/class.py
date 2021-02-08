# 클래스 (스타크래프트 예시)

# 유닛 '마린' 생성
name = "마린"
hp = 40
damage = 5

print("{} 유닛이 생성되었습니다.".format(name))
print("체력 {}, 공격력 {}\n".format(hp, damage))

# 유닛 '시즈탱크' 생성
tank_name = "탱크"
tank_hp = 150
tank_damage = 35

print("{} 유닛이 생성되었습니다.".format(tank_name))
print("체력 {}, 공격력 {}\n".format(tank_hp, tank_damage))


# 유닛 '시즈탱크2' 생성
tank2_name = "탱크"
tank2_hp = 150
tank2_damage = 35

print("{} 유닛이 생성되었습니다.".format(tank2_name))
print("체력 {}, 공격력 {}\n".format(tank2_hp, tank2_damage))


def attack(name, location, damage):
    print("{} : {} 방향으로 적군을 공격합니다. [공격력 {}]".format(name, location, damage))


attack(name, "1시", damage)
attack(tank_name, "1시", tank_damage)
attack(tank2_name, "1시", tank2_damage)

# 근데 이런 탱크가 많이 생성해야한다면? 매번 만들어줘야하나?
# 이럴 때 사용하는게 class
# 이걸 class로 다시 만들어보자!

# __init__은 파이썬에서 쓰이는 생성자다. 예시의 경우 마린이나 탱크같은 객체가 만들어질 때 자동으로 생성되는 부분이다.
# 어떤 class로부터 만들어지는 애들을 객체라고 표현하고, 이 때 마린과 탱크는 Unit class의 인스턴스라고 표현한다.
# 객체가 생성될 때는 기본적으로 init 함수에 정의된 개수와 동일하게 해야한다.(self 제외)


class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{} 유닛이 생성 되었습니다.".format(self.name))
        print("체력 {}, 공격력 {}".format(self.hp, self.damage))


marine1 = Unit("마린", 40, 5)
marine2 = Unit("마린", 40, 5)
siz_tank = Unit("탱크", 150, 35)


# 멤버 변수
# class 안에서, self.name, self.hp, self.damage 가 있는데 이런 애들이 바로 멤버 변수가 되는 것이다.
# 즉, 멤버 변수다 라고 한다면, class에서 정의된 변수고 그 변수를 가지고 초기화를 할 수 있고 실제로 쓸 수도 있는 것이다.

# 레이스 유닛
wraith1 = Unit("레이스", 80, 5)
print("유닛 이름 : {}, 공격력 : {}".format(wraith1.name, wraith1.damage))
# 클래스 외부에서 이런 식으로 사용이 가능하다.

# 마인드 컨트롤 예시
wraith2 = Unit("빼앗은 레이스", 80, 5)
wraith2.clocking = True
# clocking이라는 변수는 사실 없다. 그런데 외부에서 clocking이라는 변수를 추가로 할당한 것.

if wraith2.clocking == True:
    print("{}는 현재 클로킹 상태입니다.".format(wraith2.name))

# 이런식으로 파이썬에서는 어떤 객체에 추가로 변수를 외부에서 만들어서 쓸 수가 있다.
# 그런데 차이점은 wraith2 에는 클로킹이 있는데, wraith1에는 없는 것이다.
# 만약 위의 if문에서 wraith1의 클로킹 여부를 확인했다면 프로그램이 죽었을 것.


# 메소드
# attack 과 damaged라는 메서드를 만들어서 적용해보기.

# 공격 유닛 생성
class AttackUnit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

    # self는 자기 자신을 의미하는 것이고, 클래스 내에서 반드시 self를 적어주어야한다.
    # attack(self)->  이 부분
    def attack(self, location):
        print("{} : {} 방향으로 적군을 공격 합니다. [공격력 {}]".format(
            self.name, location, self.damage))

    def damaged(self, damage):
        print("{} : {} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{} : 현재 체력은 {} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{} : 파괴되었습니다.".format(self.name))


# 파이어뱃 생성
firebat1 = AttackUnit("파이어뱃", 50, 16)
firebat1.attack("5시")

# 공격 2번 받는다고 가정
firebat1.damaged(25)
firebat1.damaged(25)

# 상속
# damage가 없는 유닛을 생성해야한다 해보자.
# 그런데  유닛들마다 겹치는 부분이 많은데 굳이 매번 다 입력을 해주어야하나?
# 그래서 공통된 부분들만 상속시켜줄수가 있다.


class NoDamageUnit:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

# 힐러 유닛 생성
# 상속할 클래스를 적어준다.


class HealerUnit(NoDamageUnit):
    def __init__(self, name, hp, heal):
        NoDamageUnit.__init__(self, name, hp)
        self.heal = heal


medic1 = HealerUnit("ㅁㅔ딕", 40, 15)
