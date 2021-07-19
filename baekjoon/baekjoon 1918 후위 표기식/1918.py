# 스택 두개를 두고 첫번째 스택에서는 팝만 두번째 스택에는 쌓기만 한다.

# 연산자를 발견하면 팝해서 맨 뒤에 푸시
# '(' 만나면 +1 ')'만나면 -1로 괄호 카운트를 둔다
# 연산자용 카운트도 만들어서 만약 '('를 만나면 연산자용 카운트도 +1 씩해준다.
# 이후에 연산자를 뒤에 푸시해줄때, 연산자용 카운트 만큼 뒤에서 푸시해주도록 한다.

# 만약 괄호 카운트가 0인 경우라면 연산자를 만났을 때 그냥 넘어간다. 연산자용 카운트도 0으로 초기화


stack = list(input())
result = []
box_cnt = 0
opr_cnt = 0
str_cnt = 0

operater = ['+', '-', '/', '*']
box = ['(', ')']


print(stack)

for i in range(len(stack)):
    if stack[i] in operater:
        if box_cnt == 0:
            result.append(stack[i])
            opr_cnt += 1
        else:
            result.insert(-opr_cnt, stack[i])
            print("operater : ", -opr_cnt, result)
    elif stack[i] == '(':
        box_cnt += 1
    elif stack[i] == ')':
        box_cnt -= 1
    else:
        if box_cnt == 0:
            str_cnt = len(result)-1
        else:
            result.insert(str_cnt, stack[i])
            print("string : ", str_cnt, result)
            str_cnt += 1


print(result, sep='')
# A+(B*C)
# (A+(B*C))
# (A+B)*(C-D)
# (A+(B*C))-(D/E)
