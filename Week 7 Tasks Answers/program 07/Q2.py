def func_union(arg_one,arg_two):
    
    return sorted(list(set(arg_one) | set(arg_two)))


def func_intersection(arg_one,arg_two):
    
    return sorted(list(set(arg_one) & set(arg_two)))


def func_sym_difference(arg_one,arg_two):
    
    return sorted(list(set(arg_one) ^ set(arg_two)))



string_1 = "cheese"
string_2 = "cheesy"

print(func_union(string_1,string_2))
print(func_intersection(string_1,string_2))
print(func_sym_difference(string_1,string_2))
