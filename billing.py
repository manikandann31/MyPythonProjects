x=float(input("Enter the amount: "))
price=x+((18/100)*x)
print ("amount added gst is :",price)
if price>=1000:
    
    discount=price*0.1
    total=price-discount
    print("Amount payable is :",total,"discount applied")
else:
    print("The amount payable is : ",price,"no discount")