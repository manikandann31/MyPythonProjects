a=0
b=0
def add(a,b):
    a=int(input("Enter firsst value to add: "))
    b=int(input("Enter second value to add: "))
    print(a+b)  #the print function used here to show the ourput to the user.

def sub(a,b):
    a=int(input("Enter first value to sub:"))
    b=int(input("Enter second value to sub:"))
    return a-b #the return function just throw out the value of the opeation to the next assigned variable
result=sub(a,b)
print(result)

