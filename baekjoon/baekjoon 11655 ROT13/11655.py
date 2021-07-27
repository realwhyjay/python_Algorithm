# str = list(input())
# result = ""
# for i in range(len(str)):
#     if str[i] == ' ':
#         result += ' '
#     elif ord('a') <= ord(str[i]) <= ord('z'):
#         temp = ord(str[i])+13
#         if temp > ord('z'):
#             temp = (temp % ord('z'))+ord('a')-1
#         result += chr(temp)
#     elif ord('A') <= ord(str[i]) <= ord('Z'):
#         temp = ord(str[i])+13
#         if temp > ord('Z'):
#             temp = (temp % ord('Z'))+ord('A')-1
#         result += chr(temp)
#     else:
#         result += str[i]

# print(result)

test = input()
print(test[0].islower)
