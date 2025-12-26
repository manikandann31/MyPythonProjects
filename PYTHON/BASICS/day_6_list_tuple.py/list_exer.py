#1 Sum of Elements
numbers=[2,11,17,80,36,75,88]
total=0
for i in numbers:
    total=total+i
print("total sum of items:",total)
#2 find largest of the list
largest=0
for i in numbers:
    if i>largest:
        largest=i
print("The largest in the list is:",largest)
#3 count no.of even numbers in list.
count=0
for i in numbers:
    if i%2==0:
        print(i)
        count+=1
print("The no.of even number in the list is:",count)
#4 remove duplicate element from list
names=["allen","tom","mose","allen","tom","mose","benny"]
unique_name=[]
for i in names:
    if i not in unique_name:
        unique_name.append(i) 
print("Thee unique list is:",unique_name)
#separate a single list into even and odd list.
#use a list numbers in above example
odd_list=[]
even_list=[]
for num in numbers:
    if num%2==0:
        even_list.append(num)
    else:
        odd_list.append(num)
print("The even numbers in the list is:",even_list)
print("The odd numbers in the list is:",odd_list)


    
