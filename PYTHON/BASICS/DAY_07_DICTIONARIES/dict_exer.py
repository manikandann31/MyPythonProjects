#task1 create and access
data={
    "name":"allen",
    "age":25,
    "role":"analyst"
}
for key,value in data.items():
    print(key,value)
#task2 update values
#update the role from analyst to senior analyst.
data.update({"role":"senior analyst"})
print(data)
#input syntax
char={}
n=int(input("Enter no.of key value pair:"))
for i in range(n):
    key=input("Enter a key:")
    value=input("Enter a value:")
    char[key]=value
print(char)
#take a string as a input , and count the frequency of character
s=input("Enter a string to count frequency: ")
dic={}
for char in s:
    if char in dic:
        dic[char]+=1
    else:
        dic[char]=1
print(dic)
#enter a sentence to count repeatability of word
s=input("Enter a sentence: ")
dic={}
spl=s.split(" ")
print(spl)
for char in spl:
    if char in dic:
        dic[char]+=1
    else:
        dic[char]=1
print(dic)
n=int(input("Enter no.of subjects:"))
mark={}
for i in range(n):
    key=input("Enter your subject:")
    value=int(input("Enter your mark:"))
    mark[key]=value
print(mark)
total=0
for m in mark.values():
    total+=m
print("your total mark is :",total)
avg=int(total/n)
print("average",avg)
