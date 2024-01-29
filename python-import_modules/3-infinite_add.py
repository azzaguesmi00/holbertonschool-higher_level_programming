#!/usr/bin/python3
if __name__ == "__main__":
	import sys
	argv = sys.argv
	num = 0
	for index in range(1, len(argv)):
		num += int(argv[index])
	print("{}".format(num))
