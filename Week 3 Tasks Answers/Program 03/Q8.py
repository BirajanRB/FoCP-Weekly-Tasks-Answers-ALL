number = int(input("Enter the table required:"))
if number <= 12 and number>=0:
    for i in range(number+1):
        print("7x{}={}".format(i,7*i))
elif number<0:
    i=12
    while(i>=0):
        print("7x{}={}".format(i,7*i))
        i -= 1