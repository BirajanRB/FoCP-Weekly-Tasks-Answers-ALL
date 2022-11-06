while(1):
    password = input("Enter a new password: ")

    BAD_PASSWORDS = ['password', 'letmein', 'sesame', 'hello', 'justinbieber']
    
    if password in BAD_PASSWORDS:
        print("Enter another password!")
    else:
        if len(password)>=8 and len(password)<=12:
            
            re_password = input("Re-Enter password: ")
            if password == re_password: 
                print("Password Set!")
                break
            else:
                print("Passwords do not match!")
                
        else:
            print("Please Enter A password between 8 and 12 characters long!")

