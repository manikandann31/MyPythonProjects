correct_password = "111"
attempts = 0
while attempts < 3:
    password = input("Enter your password: ")
    if password == correct_password:
        print("Access granted")
        break
    attempts += 1
else:
    print("Access denied. Too many attempts")

