n = int(input())
parentNode = [-1]*(n+1)
tree = {}
root = 0

# 입력값으로 트리 만들기
for _ in range(n):
    node, left, right = map(int, input().split())
    tree[node] = [left, right]
    if left != -1:
        parentNode[left] = node
    if right != -1:
        parentNode[right] = node

# 루트 찾기
for i in range(1, n+1):
    if parentNode[i] == -1:
        root = i

# 각 레벨의 최소, 최대 idx를 저장한다.
level_min = [n]*(n+1)
level_max = [0]*(n+1)
level = [0]*(n+1)
level[root] = 1
cur = 0


def inorder(key):
    global cur
    if tree[key][0] != -1:
        level[tree[key][0]] = level[key]+1
        inorder(tree[key][0])

    cur += 1

    if level_min[level[key]] > cur:
        level_min[level[key]] = cur
    if level_max[level[key]] < cur:
        level_max[level[key]] = cur

    if tree[key][1] != -1:
        level[tree[key][1]] = level[key]+1
        inorder(tree[key][1])

    return


inorder(root)

result = 0
result_idx = 0

for i in range(1, n+1):
    diff = level_max[i] - level_min[i]+1
    if result < diff:
        result = diff
        result_idx = i

print(result_idx, result)

print(level)
print(level_max)
print(level_min)
