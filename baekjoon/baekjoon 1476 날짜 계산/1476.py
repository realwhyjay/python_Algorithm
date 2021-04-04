e, s, m = map(int, input().split())
E, S, M = 1, 1, 1
count = 0

while(True):
    count += 1

    if E == e and S == s and M == m:
        print(count)
        break

    E += 1
    S += 1
    M += 1

    if(E == 16):
        E = 1
    if(S == 29):
        S = 1
    if(M == 20):
        M = 1

#    print("E,S,M : {} {} {}".format(E, S, M))

#print("e,s,m : {} {} {}".format(e, s, m))

# print(count)


count = 1
while True:
    if(count-e) % 15 == 0 and (count-s) % 28 == 0 and (count - m) % 19 == 0:
        print(count)
        break
    count += 1
