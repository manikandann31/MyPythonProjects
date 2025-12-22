word=input("Enter a sentence: ")
br_word=word.split(" ")
max_len=0
longest_word=""
for i in range(0,len(br_word)):
    if max_len<len(br_word[i]):
        max_len=len(br_word[i])
        longest_word=br_word[i]
print("The length of longest string is :",+max_len)
print("The longest sentnce is:",longest_word)

