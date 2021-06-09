import sys
input = sys.stdin.readline

n = int(input())
stack = []
for _ in range(n):
    command = list(input().split())
    if command[0] == 'push':
        stack.append(command[1])
    elif command[0] == 'pop':
        if not stack:
            print(-1)
        else:
            print(stack.pop())
    elif command[0] == 'top':
        if not stack:
            print(-1)
        else:
            print(stack[-1])
    elif command[0] == 'size':
        print(len(stack))
    else:
        print(1 if not stack else 0)
