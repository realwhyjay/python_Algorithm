kg = int(input())
max = (kg//3)+1
bag = max

for i in range((kg//5)+1):
    for j in range((kg//3)+1):
        if ((5*i)+(3*j)) == kg:
            bag = i+j if (i+j) < bag else bag

print(bag if bag != (kg//3)+1 else -1)
8
