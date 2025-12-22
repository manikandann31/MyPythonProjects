#couont the character
ch="encyclopedia"
count=0
for i in ch:
    count+=1
print(count)
#count the no.of vowels
cha="encyclopedia"
count=0
for i in "aeiou":
    count=count+1
print(count)
#reverse a string
s=("Encyclopedia")
i=len(s)-1
while i>=0:
    print(s[i],end="")
    i-=1
#palindrome
s="python"
i=0
j=len(s)-1
while i<j:
    if s[i]==s[j]:
        print("is palindrome")
        break
    else:
        print("not palindrome")
        break
#count no.of words
letter="data analytics"
count=0
for i in letter:
    count+=1
print(count)


#checking character frequency
char = "banana"
for i in range(len(char)):
    count = 0
    for j in range(len(char)):
        if char[i] == char[j]:
            count += 1
    print(char[i], "=", count)
#remove duplicates
s="banana"
new=''
for i in s:
    if i not in new:
        new=new+i
print(new)
