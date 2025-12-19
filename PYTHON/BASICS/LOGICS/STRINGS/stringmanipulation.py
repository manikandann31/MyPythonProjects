mobile="8610665563"
print(mobile[2:])
print(mobile[:2])
print(mobile[-2:])
print(mobile[:-2])
print((mobile[:4])+"******")

message="your uber booking id is : UB1234. please keep it safe."
"""now you have to take out the booking id from the emtire message (using split () function)"""
id=message.split(":")[1].split(".")[0].strip()
print(id)

promo_code="use coupen code Zomato100 to get 50 off on your first order"
"""you have to rxtract the coupen code from the given promo message and give offer to th specific user, and you already know thee coupen code"""
if "Zomato100" in promo_code:  
    print("offer applied")

feedback="the driver is polite and the ride was smooth"
"""now  the tASK is to find the index position of the word polite in the feedback"""
print(feedback.find("polite"))