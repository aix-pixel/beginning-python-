sentence = input("enter the sentence: ")
count = 0
for ch in sentence:
    if ch.isalpha():

        count += 1
    if ch.isdigit():
        count  += 1    
print(count)        