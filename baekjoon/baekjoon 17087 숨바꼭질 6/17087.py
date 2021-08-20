def GCD(a, b):
    if a < b:
        a, b = b, a
    if b == 0:
        return a
    else:
        return GCD(b, a % b)


n, s = map(int, (input().split()))
location = list(map(int, (input().split())))

for i in range(len(location)):
    location[i] = abs(s - location[i])

GCDresult = location[0]

for j in range(len(location)):
    GCDresult = GCD(location[j], GCDresult)

print(GCDresult)
