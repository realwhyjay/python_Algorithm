document = input()
text = input()
index = 0
count = 0

while index <= len(document):
    if document[index:index+len(text)] == text:
        count += 1
        index += len(text)
    else:
        index += 1

print(count)
