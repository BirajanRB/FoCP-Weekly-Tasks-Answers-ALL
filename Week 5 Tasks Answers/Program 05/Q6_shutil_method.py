import shutil
import sys

#(src,dest)
#copyfile
#copy
#copy2

if 1<len(sys.argv)<3:
	File = sys.argv[1]
	File_copy = File.split(".")
	File_2_name = File_copy[0]+"_copy"+"."+File_copy[1]

	shutil.copyfile(sys.argv[1],File_2_name)

else:
	print("invalid number of file name")