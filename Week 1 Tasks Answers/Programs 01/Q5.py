Lab_group = 24

Students = [113,175,12]

for i in range(0,3):
    print("The number of full lab groups in group %d is %d"%(i+1,Students[i]/Lab_group)) 
    print("The number of left over students in group %d is %d \n"%(i+1,Students[i]%Lab_group)) 
    