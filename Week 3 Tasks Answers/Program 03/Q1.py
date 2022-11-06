user_name = input("Hello, what is your name? ")

print("Hello, Stranger!" if user_name == "" else "Hello, {}. Good to meet you!".format(user_name))
    