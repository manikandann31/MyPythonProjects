"""#1 reverse a number(without while loop)
num=(input("Enter the number: "))
print(num[::-1])
#1 reverse a number(using while loop)
num=int(input("Enter the number to reverse: "))
reversed_number=0
while num>0:
    remaining_digit=num%10                               #takting the last digit from the input number
    reversed_number=reversed_number*10+remaining_digit   #if input is 123, it convert 0*10+3, so it moves the last digit to first, similarly we add the next digit and so on 
    num=num//10                                          #this floor division removes the last digit from input, and give number to next iteration without the  last digit 
print(reversed_number)
#3 count the digit 
num=int(input("Enter number to count the digit: "))
count=0
while num>0:
    count=count+1
    num=num//10
print(count)
#4 count the character in a string 
ch=input("Enter a character to count: ")
i=0
count=0
while i<len(ch):
    count+=1
    i+=1
print(count)
#5 sum of digits
digit=input("Enter number to sum its digit: ")
i=0
sum=0
while i<=len(digit):
    sum=sum+int(i)
    i+=1
print(sum)"""





