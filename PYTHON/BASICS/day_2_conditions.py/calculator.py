a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
op=input("what operation do you want to do(add,sub,mul,div,mod) with the two numbers: ")
if op.lower()=="add":
    print(a+b)
elif op.lower() =="sub":
    print(a-b)
elif op.lower() =="mul":
    print(a*b)
elif op.lower() =="div":
    print(a/b)
elif op.lower() =="mod":
    print(a%b)
else:
    print("Enter a valid operation")


"""
What I learned today:
1. How if-elif-else flows
2. Why condition order matters
3. How logical operators affect decisions
"""


