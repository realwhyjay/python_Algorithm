n, m = map(int, input().split())
castle = []

for _ in range(n):
    castle.append(input())

row = [0] * n
colum = [0] * m

for i in range(n):
    for j in range(m):
        if castle[i][j] == 'X':
            row[i] = 1
            colum[j] = 1

row_count = 0
for i in range(n):
    if row[i] == 0:
        row_count += 1

colum_count = 0
for i in range(m):
    if colum[i] == 0:
        colum_count += 1

print(max(row_count, colum_count))
