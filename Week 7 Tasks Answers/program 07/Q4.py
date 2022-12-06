from string import ascii_lowercase
letter_dict= {x : 0 for x in ascii_lowercase}

message = (input("Enter the message: ")).lower()
message_lst = [i for i in message if i.isalpha()]

for i in message_lst:
         letter_dict[i] += 1

sorted_dict = sorted(letter_dict.items(),key = lambda x : x[1], reverse=True)
#sorting using the 2nd item of the returned tuple.
#returned as a list of tuple.

most_common_letters = dict(i for i in sorted_dict[0:6])

print("The six most common letters are:")
for i in most_common_letters:
    print(i ,",number of times appeared:", most_common_letters[i])