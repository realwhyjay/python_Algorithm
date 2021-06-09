import sys
input = sys.stdin.readline

n = int(input())
queue = []
for _ in range(n):
    command = list(input().split())
    if command[0] == 'push_back':
        queue.append(command[1])
    elif command[0] == 'push_front':
        queue.insert(0, command[1])
    elif command[0] == 'pop_front':
        if not queue:
            print(-1)
        else:
            print(queue.pop(0))
    elif command[0] == 'pop_back':
        if not queue:
            print(-1)
        else:
            print(queue.pop())
    elif command[0] == 'back':
        if not queue:
            print(-1)
        else:
            print(queue[-1])
    elif command[0] == 'front':
        if not queue:
            print(-1)
        else:
            print(queue[0])
    elif command[0] == 'size':
        print(len(queue))
    else:
        print(1 if not queue else 0)
