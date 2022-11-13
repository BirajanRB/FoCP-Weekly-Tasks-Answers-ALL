def letter_func(str_arg):
    """A function that has a single string as its parameter, and returns the number of uppercase letters, and the number of lowercase letters in the string."""
    
    import string
    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    
    upper_num = 0
    lower_num = 0
    
    for i in str_arg:
        if i in uppercase:
            upper_num += 1
        elif i in lowercase:
            lower_num += 1
            
    return upper_num, lower_num

print(letter_func("Computer Science"))