sentence = input("Enter a sentence: ")
count = 0
inside_word = False
for char in sentence:
    if char != " " and not inside_word:
        count += 1
        inside_word = True
    
print (count)        
    