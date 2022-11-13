tempature = ["55C","10C","100C","200C","20C","5C"]
data = []
for i in tempature:
    data.append(int(i[0:-1])) 

print("The maximum: ",max(data),"C",sep="")
print("The minimum: ",min(data),"C",sep="")

from statistics import mean
print("The mean: ",mean(data),"C",sep="")

    

