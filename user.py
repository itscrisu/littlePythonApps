name = input("Enter your name please: ")

if len(name) < 3:
    print("Your name should have at least 3 characters")
elif len(name) > 50:
    print("Your name should not have more than 50 characters")
else:
    print("Good name :)")
