#immutable
#faster than list because it allow no modification insid it , so it is faster to access
#tuple is used as key  dictionary concept
data=("uber","airport",450.00,"completed")
#access the tuple data:
print(data[1])
#travel through the tuple:
for item in data:
    print(item)
#to find length of the tuple:
print(len(data))
#to find index positoin of element
print("The index of your data is:",data.index(450.00))
#to find the count of a perticular item in a list 
print(data.count(450.00))
data[2]=400.00 # this shows the error of "'tuple' object does not support item assignment"cuz tuple is immutable
