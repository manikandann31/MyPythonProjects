
#stringfunctions 
name="Manikandan N"
print(name.lower())
print(name.upper())
print(name.title())
print(name.capitalize())

#masking command 
mobile='8610665563'
masked = mobile[:2]+"******"+mobile[-2:]
print(masked)

#title command 
song="die MountaiN DEW"
author="maNIkandAn"
formatted=f"{song.title()} - {author.title()}"
print(formatted)

#replace command 
location  = str(input("Enter the location to pick up"))
new_location=str(input("Enter updated location to pick up: "))
fixed_location=location.replace(location,new_location)
print(fixed_location) 

#split  command 
password="mani.123"
text=password.split(("."))
print (text)
message="This is your user id: 17265, Do not share with anyone" #the task is to print the user id from the messagge"
user_id=message.split(":")[1].split(",")[0].strip() #strip function removes the extra space
print(user_id)
offer_msg="use the coupencode zomato100 to gain 100 off on your first order" #the task is  to finnd the coupn code
if "zomato100" in offer_msg:
    print("offer available")
feedback = "The driver was polite and the ride was smooth"
position=feedback.find("polite")
print(position)
#wordcount
word="Chrome can now read web pages aloud. Words on the page are highlighted to help you follow along. Read aloud is best for content like news stories, articles, or even PDFs.To use read aloud, right-click on a page, and select Open in reading mode. This opens the side panel, which has controls you can use for read aloud.Click the Play  button.You can adjust the voice  , speed , and highlight style  in the toolbar next to the Play button."
word_count=len(word.split(" "))
print(word_count)