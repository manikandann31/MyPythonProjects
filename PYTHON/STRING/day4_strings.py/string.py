name="dAtA AnAlYsT I n Python"
print(name.lower())
print(name.upper())
print(name.capitalize())
print(name.title())
print(name.split("I")[0])             #it splits the sentence using the delimitor - I, the letters before I is considered as index 0 and after I is considered as 1. 
print(name.split("I")[1].strip())     #strip() function is used to remove the space in before and after of th sentence.
location=input("Enter your location: ")
updated_location=input("Enter your updated location: ")
print(location.replace(location,updated_location))

#to check a perticular word is present in a sentence(You alrady know what the word is)
sentence="python is so easy to learn and understand"
if "python" in sentence:
    print("yes present")
else:
    print("no word")

#to take out and print a perticular word from a sentence
sentence="what is the easiest programming language? python, is the easiest language."
print(sentence.split("?")[1].split(",")[0].strip())