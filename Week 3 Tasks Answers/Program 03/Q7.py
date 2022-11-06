number = int(input("Enter the table required:"))
if number <= 12 and number>=0:
    for i in range(number+1):
        print("7x{}={}".format(i,7*i))
else:
    print("Number should be between 0 and 12 inclusive!")