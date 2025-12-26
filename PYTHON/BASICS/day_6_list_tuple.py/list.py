songs=["song1","song2","song3","song4"]

#list operations
# 1.append(),, add the song to last index position of the list
songs.append("song5")
print("After append",songs)
#2 insert(),,insert element into the list in the desired location.
songs.insert(2,"song 2.5")
print("After insertion of song 2.5:",songs)
#3 remove(),, it removes the specific element from specific position
songs.remove("song 2.5")
print("After removal of song 2.5:",songs)
#4 pop(),,it simply removs th last element of the list 
songs.pop()
print("After pop:",songs)
#pop vs remove : pop is used to remove last index of the list, but remove is used for specific removal of items from the list.
#5.reverse(),,it reverse the entire list 
#songs.reverse()
#print("Reversed list: ",songs)
#6. count ,, to find the index positon of the specific element. ex: find index of song 4,note: the syntax is quite different from thee above.
print(songs.count("song4")) # it returns the index value 1 because the string is reversed in revious function, so song 4 gt indx positon 1.

movie=["movie1","movie2","movie3","movie4","movie5","movie6"]
#slicing: used to take specific element of index.
#to show the first two movies of the list.
print("The first two element of the list movie is:",movie[:2])
#to show the last two movies of the list.
print("The last two element of the list movie is:",movie[-2:])
#list iteration
#to print the all elements of list one by  one 
for i in movie:
    print("The movie is: ",i.upper())
#to print song along with movie ex:movie1 song1.
for i in range(len(songs)):
    value=movie[i]+songs[i]
    print(value)
#to check an item is present in a list
if "movie2" in movie:
    print("Yes present")
else:
    print("it is not present in the list ")
#to update values of the list 
menu=["idli","dosa","vada","sambar"]
print("The menu is:",menu)
menu[0]="pongal"
print("Th updated menu is:",menu)
# to print index value of all items in the list we use for loop with two parameter and aslso a enumerator function, lets see
for i,item in enumerate(menu):
    print(f"{i}:{item}")

