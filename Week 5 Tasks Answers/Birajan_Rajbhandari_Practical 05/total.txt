#importing the sys module
import sys

#accessing the command line arguments vai "sys.argv"
count = len(sys.argv)

#first element of the list being the file-name
total_elements = count-1
total = 0

#loops until the 2nd element is reached
while count > 1:
	count -= 1
	total += float(sys.argv[count])

print("Total is", total)

#checks whether the number of elements are more then 0 or not.
if total_elements == 0:
	#case where no command line argument were given
	print("no arguments were provided.")
else:
	#case where the number of elements is greater than 0.
	print("The average is",total/(total_elements))

