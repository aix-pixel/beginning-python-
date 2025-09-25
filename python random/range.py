sentence = input("enter the sentence: ")
count = 0
for char in sentence:
    if char.isalpha():
        count += 1

print(count)