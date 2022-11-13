def last_input(input_data):
    """A function that takes a string parameter and returns it with the last character removed."""
    if len(input_data)<2:
        return input_data
    else:
        return input_data[0:-1]

print(last_input("Hello World 1"))
print(last_input("F"))
