def range_func(i_num):
    """A function that accepts a single integer as a parameter and returns True if the integer is in the range 0 to 100 (inclusive), or False otherwise."""
    if i_num in range(0,101):
        return True
    else:
        return False
    
print(range_func(0))
print(range_func(100))
print(range_func(101))

