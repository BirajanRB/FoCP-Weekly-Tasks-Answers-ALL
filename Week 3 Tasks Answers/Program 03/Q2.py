password = input("Enter a new password: ")
re_password = input("Re-Enter password: ")

if password == re_password:
    print("Password Set!")
else:
    print("Passwords do not match!")