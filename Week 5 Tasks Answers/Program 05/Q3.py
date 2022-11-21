import sys

if len(sys.argv) < 2:
	print("No argument given")
else:
	arg = sys.argv[1:]
	arg.sort(key = len)
	print("Shortest argument:",arg[0])

