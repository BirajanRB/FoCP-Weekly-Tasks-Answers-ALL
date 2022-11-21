import sys
from statistics import mean

if len(sys.argv) < 2:
	print("No argument entered.")
else:
	
	temp = []

	for i in sys.argv[1:]:
		temp.append(int(i))

	print("The maximum temperature: ",max(temp),"Degree",sep="")
	print("The minimum temperature: ",min(temp),"Degree",sep="")
	print("The mean: ",mean(temp),"Degree",sep="")
