password = input("Enter a new password: ")

if len(password)>=8 and len(password)<=12:
    re_password = input("Re-Enter password: ")

    if password == re_password:
        print("Password Set!")
    else:
        print("Passwords do not match!")  

else:
    print("Please Enter A password between 8 and 12 characters long!")

