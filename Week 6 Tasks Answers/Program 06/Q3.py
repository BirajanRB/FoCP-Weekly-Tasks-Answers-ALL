def prime_num(int_val):
    """A function that determines if a given integer is a prime number."""
    
    for i in range(2,int_val):
            if int_val%i == 0:
                print("The given integer is not a prime number.")
                break
    else:
        print("The given integer is a prime number.")
    
            
prime_num(13)