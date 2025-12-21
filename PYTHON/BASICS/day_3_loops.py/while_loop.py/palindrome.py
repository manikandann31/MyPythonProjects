#palindrome(without while loop)
s=input("Enter a letter to check it is a palindrome: ")
reversed_s=s[::-1]
if s==reversed_s:
    print("is palindrome")
else:
    print("no palindrome")
#palindrome(using while loop)
s=input("Enter the letter to check it is a palindrome: ")
i=0
j=len(s)-1
while i<j:
    if s[i]!=s[j]:
        print("it is not palindrome")
        break
    else:
        print("it is palindrome")
        break

