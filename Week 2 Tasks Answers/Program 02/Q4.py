total_sweets = int(input("Number of sweets? "))
total_students = int(input("How many students? "))

sweets_to_give = total_sweets//total_students
sweets_left = total_sweets%total_students


if(sweets_left<=1):
    print("Each pupil will get %d sweets and %d sweet would be left over."%(sweets_to_give,sweets_left))

else:
    print("Each pupil will get %d sweets and %d sweets would be left over."%(sweets_to_give,sweets_left))