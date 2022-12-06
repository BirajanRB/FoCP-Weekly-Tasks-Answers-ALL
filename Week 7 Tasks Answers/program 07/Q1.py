def sort_list(arg_str):
    """A function that takes a string as a parameter and returns a sorted list of all the unique letters used in the string."""
    
    return sorted(list(set(arg_str)))

print(sort_list("cheese"))