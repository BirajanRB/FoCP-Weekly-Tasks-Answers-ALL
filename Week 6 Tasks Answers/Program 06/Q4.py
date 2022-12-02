def en_func_original(msg_var):
    """a function that takes a string containing a message and "encrypts" it"""
    lst = msg_var.split(" ")
    return "".join(lst)[::-1]

def en_func_ver_tony(msg_var):
    lst = [i for i in msg_var if i.isalpha()]
    lst.reverse()
    return "".join(lst)




val ="Its a great day to have fun."

print(en_func_original(val))

print(en_func_ver_tony(val))