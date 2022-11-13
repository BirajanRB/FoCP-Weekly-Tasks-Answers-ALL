data = []
while(1):
    i = input("Enter Tempature: ")
    if i == "":
        break
    data.append(int(i[0:-1])) 

print("The maximum: ",max(data),"C",sep="")
print("The minimum: ",min(data),"C",sep="")

from statistics import mean
print("The mean: ",mean(data),"C",sep="")


    

