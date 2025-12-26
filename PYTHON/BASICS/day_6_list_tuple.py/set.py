#another data set like list and tuple , it is almost similar to those, but it doesnot allow duplication of data.
cities={"chennai","mumbai","delhi","chennai","mumbai","hydrabad"} #this is set
print(cities) #the result doesnot print all element of the set, instead it remove duplicate and print  it 

#we can able to remove duplicate from a list by convrting it into a set,for ex:
cities=["chennai","mumbai","delhi","chennai","mumbai","hydrabad"] # this is list
unique_cities=set(cities)
print(cities)
print(unique_cities)
# union and intersection of set
num1={1,2,3,4,5,6}
num2={4,5,6,7,8,9}
print(num1.union(num2))
print(num1.intersection(num2))
#if you want to append the set, you can just give the item for append, the set datatye will auto indec the item to random positiion.NOTE: set doesnot have indexing system.
num2.add(10) 
print(num2)
num2.remove(10)
print(num2)