num = int(input())
people = []

for _ in range(num):
    data = list(input().split())
    people.append((int(data[0]), data[1]))

people = sorted(people, key=lambda x: x[0])

for i in people:
    print(i[0], i[1])
