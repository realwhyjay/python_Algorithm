a = input()
stack = []  # 스택
res = ''  # 출력

for x in a:
    if x.isalpha():  # 피연산자인지 아닌지 확인
        res += x
    else:
        # 괄호가 열려있는지 확인한다
        if x == '(':
            stack.append(x)
        # 곱셈(*)인지 나눗셈(/)인지 확인한뒤, 먼저 들어온 같은 우선순위의 */를 모두 결과 문자열에 추가한다
        # 현재 문자를 다시 스택에 추가한다
        elif x == '*' or x == '/':
            while stack and (stack[-1] == '*' or stack[-1] == '/'):
                res += stack.pop()
            stack.append(x)
        # +,-는 우선 순위가 제일 낮기 때문에, 자신보다 우선 순위가 높은 것들은 전부 결과 문자열에 추가한다
        # 현재 문자를 다시 스택에 추가한다
        elif x == '+' or x == '-':
            while stack and stack[-1] != '(':
                res += stack.pop()
            stack.append(x)
        # 만약 괄호가 닫혔다면, (과 )사이의 모든 연사자들을 결과 문자열에 추가하고
        # )를 pop 해준다.
        elif x == ')':
            while stack and stack[-1] != '(':
                res += stack.pop()
            stack.pop()

# 마지막으로 스택안에 남아있는 값들을 결과 문자열에 추가한다.
while stack:
    res += stack.pop()
print(res)
