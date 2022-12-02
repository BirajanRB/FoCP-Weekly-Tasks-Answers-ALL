def fact(int_val):
    """Returns all factors of the given argument value."""
    
    list_test = [x for x in range(1,int_val+1) for j in range(1,int_val+1) if x*j == int_val]
    
    return list_test

print(fact(24))

