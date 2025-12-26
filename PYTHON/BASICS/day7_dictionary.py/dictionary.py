student={
    "reg_no":422222104031,
    "name":"manikandan",
    "dob":2003,
    "course":"cse",
    "bus_no":[1,18,12,14],
    "destination":["tirukoilur","villupuram"]
}
#to access specific value in a dictionary, it has two ways 
#way 1 , but it return error if your searching element is not in the dictionary
print(student["dob"])
#way 2 (safest), it does not return error when your searching element is not in the dict. instead it return null and conrinue the program execution.
print(student.get("dob"))
# if you want all keys(lookups) from the dictionary
print(student.keys())
#if you want all values from the dictionaries
print(student.values())
#to iterate over the dictionary
for key,value in student.items():
    print(key,"=",value)
#update ()  functionn in dict update the key value if the key valu is already exist, else it simply add to that dict.
student.update({"cgpa":8.1})
print(student)
student.update({"cgpa":9.1}) # as i said , it update the cgpa value now.
print(student)
stu={
    "reg_no":422222104031,
    "name":"manikandan",
    "dob":2003,
    "course":"cse",
    "bus_no":[1,18,12,14],
    "destination":["tirukoilur","villupuram"],
    "reg_no":80311402 #yet this is duplicate of the key(reg_no), but it was updated .so python print the updated value
}
print("your updated dict is :",stu) # it print the updated reg_no
for k,v in stu.items():             #use loop to print the key value one by one 
    print(k,":",v)
#if you want to acess a single perticulaar value from a mul valu of a key value set
print("The first destinatioon is :",stu["destination"][0])
print("The second destinatioon is :",stu["destination"][1])
#to print all element of perticular key:ex, we have to print all valus of bus no
for item in stu["bus_no"]:
    print(item)
#get input for a dictionary
d = {}
n = int(input("Enter number of elements: "))
for i in range(n):
    key = input("Enter key: ")
    value = input("Enter value: ")
    d[key] = value
print(d)

