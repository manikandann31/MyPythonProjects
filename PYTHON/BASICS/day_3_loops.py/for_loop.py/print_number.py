#1 printing numbers from user specification

n=int(input("Enter the number you want to print the series to : "))
for i in range(1,n+1):
    print(i)

m=int(input("Enter the number you want to print the series from: "))
n=int(input("Enter the number you want to print the series to : "))
for i in range(m,n+1):
    print(i)

#2 print all even numbers between a and b 
a=int(input("Enter the number you want to print the series from: "))
b=int(input("Enter the number you want to print the series to : "))
for i in range(a,b):
    if(i%2==0):
        print(i)
#3 sum of even numbrs between c and d (c and d are user input)
c=int(input("Enter the number you want to print the series from: "))
d=int(input("Enter the number you want to print the series to : "))
sum=0
for i in range(c,d):
    if (i%2==0):
        print(i)
        sum=sum+i  #when the indent space for this line is is remobed, then it runs and store value for eveery value of i. so you must write it in the if  block only.
print("The sum of even number is: ",sum)
#4 Count how many numbers between 1 and 100 are divisible by e(e is the user input)
e=int(input("Enter the number you want to find the mul bw 1 and 100:"))
count=0
for i in range(1,100+1):
    if i%e==0:      #unfortunately i found this is the logic for the tables printer .....haha lol
        count=count+1
print(count)
#5 count no.of character(without len() function )
ch=(input("Enter a character to count:"))
count=0
for i in ch:
    count=count+1
print(count)
#6 sum of the digits
num=(input("Enter a number to find sum of  the digits: "))
sum=0
for i in num:
    sum=sum+int(i)      #confused about type conversion and got cleared by reference on youtube vedios
print(sum)