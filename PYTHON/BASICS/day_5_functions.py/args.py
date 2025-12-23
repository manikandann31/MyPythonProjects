#it is important to know that the user doesnot want always to add two numbers only, may be they want to add n number of elements, in that situation the above progrm create parameter indeficiency.
#to ovrcome this situation we use a entitu callled *args,now wehave to write a program wusing this paramerter.
#program to add n number of elements.
def add(*args):
    total=0
    for num in args:
        total+=num
    return total
print(add(1,2,3,4,5,6,7)) # here we caan give n number of integers to add 

#for using multiple integer is ok but what about multipole string operation?
# here is the solution:  ( **kwargs ) ,, this is key value arguments.
def profile(**kwargs):
    print("User profile")
    for key,value in  kwargs.items():
        print(f"{key} : {value}")
#now call the function with key value parameters.
profile(name="mani",age=23,edu="engineering")
