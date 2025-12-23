a=int(input("Enter your first number: "))
b=int(input("Enter yout second number: "))

def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
op=0
while op<=4:
    op=int(input("Enter operation:press 1=add,2sub,3=mul 4=quit: "))
    if op==1:
        result=add(a,b)
        print("The sum of",a,"and",b,"is",result)
    elif op==2:
        result=sub(a,b)
        print("The diff of",a,"and",b,"is",result)
    elif op==3:
        result=mul(a,b)
        print("The product of",a,"and",b,"is",result)
    else:
        break
