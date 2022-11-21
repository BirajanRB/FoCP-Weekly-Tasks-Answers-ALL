import sys
from urllib import request


if 1<len(sys.argv)<3:

	Site = request.urlopen(sys.argv[1])

	#HTTP response codes

	if Site.code == 200:
		print("There is a working website at that address.")
	elif Site.code == 400:
		print("Bad Request")

	elif Site.code == 403:
		print("Forbidden")

	elif Site.code == 404:
		print("Not Found")

	else:
		print("Error!")

	
else:
	print("Invalid argument")




