#practice problms
#1.program to display last digit of a number(without indexing)
num=int(input("Enter the number: "))
if num<0:
    print("Give a positive number")
else:
    print(num%10)
#2.program to display last digit of a number(with indexing)
str_numtwo=0
numtwo=(input("Enter 2nd number: "))
print(numtwo[-1])

#3.checking a single character is vowel or not 

ch=input("Enter the letter: ")
if ch.lower() in "a,e,i,o,u":
    print("vowel")
else:
    print("not a vowel")

#4.checking a multi character is a vowel
cha=input("Enter the character: ")

for i in cha:
    if i.lower() in "aeiou":
        print("This character conatin a vowel")
        break
else:
        print("It desnot contain vowel ")
    

        
    
#5.to check a number is even or odd
num3=int(input("Enter the number: "))
if num3==0:
     print("Enter a number other than 0")
elif num3%2==0:
     print("The number is even")
else:
     print("The number is odd")

#6. to check 3rd last character is vowel or not 

char=input("Enter the character: ")
if char[-3]in "aeiou":
     print("The third last letter is a vowel")
else:
     print("Third last letter is not a vowel ")

#7.to calculate percentage of a student through 5 subjects. Take marks as input from the user.Using percentage print which grade the student has scored.
s1=int(input("Enter the sub1 mark: "))
s2=int(input("Enter the sub2 mark: "))
s3=int(input("Enter the sub3 mark: "))
s4=int(input("Enter the sub4 mark: "))
s5=int(input("Enter the sub5 mark: "))
avg=(s1+s2+s3+s4+s5)/5
print(avg)
if avg<100 and avg>90:
     print("You secured first grade")
elif avg<90 and avg>70:
     print("you secured second grade")
elif avg<70 and avg>50:
     print("You secured third grade")
else:
     print("Need more practice")

#8.to print the day based on the number input.For example: if input = 1, output = Monday
num4=int(input("Enter the number"))
if num4%7==1:
    print("monday")
elif num4%7==2:
    print("Tuesday")
elif num4%7==3:
    print("wdesday")
elif num4%7==4:
    print("Tthursday")
elif num4%7==5:
    print("friday")
elif num4%7==6:
    print("satrday")
elif num4%7==0:
    print("sunday")
else:
     print("Enter a valid number of days")

#8.count  of element in a string 
chara=input("Enter the character; ")
print(len(chara))
