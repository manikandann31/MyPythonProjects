"""There are two methods of getting input from user"""
#method 1 : 
a=int(input("enter the value: "))

#method2 : command inline arguments
import sys
full_name=sys.argv[1]
last_name=sys.argv[2]
email=full_name.lower().replace(" ",".")+last_name.lower()+ "@company.com"
print("\n---your profile---")
print("Full Name =",full_name + last_name)
print("Generated Email =",email)
