#Add Two Numbers
a=int(input("Enteer a number: "))
b=int(input("Enteer a number: "))
def add(a,b):
    return a+b
result=add(a,b)
print("The sum is :",result)
#Even or Odd Function
n=int(input("Enter a number: "))
def even(n):
    return "this is even number"
def odd(n):
    return "this is odd number"
if n%2==0:
    result=even(n)
    print(result)
else:
    res=odd(n)
    print(res)
#Create a function that takes a number and Returns its factorial
num=int(input("Enter a number for factorial: "))
i=1
def fact(num):
    fact=1
    for i in range(1,num+1):
        fact=fact*i
    return fact
result=fact(num)
print(result)
#Create a function that takes a string and Returns the reversed string
s=input("Enter a string to reverse: ")
def rev(s):
    i=len(s)-1
    rev_str=''
    while i>=0:
        rev_str=rev_str+s[i]
        i-=1
    return rev_str
result=rev(s)
print("reverse string is: ",result)

