total_students = int(input("How many students? "))
group_size = int(input("Required group size? "))

group_number = total_students//group_size
left_over_students = total_students%group_size

if(left_over_students<=1):
    print("There will be %d groups with %d student left over."%(group_number,left_over_students))

else:
    print("There will be %d groups with %d students left over."%(group_number,left_over_students))
