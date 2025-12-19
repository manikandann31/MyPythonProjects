#area of circle
print("---area of circle---")
D=int (input("Enter diameter of circle:"))
Area_of_circle=3.14*(D/2)*(D/2)
print("Area of circle is:",Area_of_circle,"msq.")

#conert celcius to farenheit
print("---temperature conversation---")
C=float(input("Enter temperature in celcius:"))
farenheit=((9/5)*C)+32
print("Your tmperature in farenheit is: ",farenheit,"'F")

#calculate simple intrest
print("---calc of simple intrest---")
P=float(input("Enter principle amount:"))
N=int(input("entr number of years:"))
R=float(input("Enter rate of intrest:"))
SI=(P*N*R)/100
print("Your simple intrest is :",SI)