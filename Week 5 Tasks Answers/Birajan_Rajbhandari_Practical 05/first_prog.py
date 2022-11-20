#Prompts the user for a number.
number = input("Enter a number: ")

#Typecasting the input str data-type into int data-type.
number = int(number)

#Prints the number entered by the user
print("The numbered entered was", number)

#Checks whether ther number entered is even or odd.
if (number % 2) == 0:
	print("That is an even number")
else:
	print("That is an odd number")
