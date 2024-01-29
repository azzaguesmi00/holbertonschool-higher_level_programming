#!/usr/bin/python3
def uppercase(str):
	for alpha in str:
		if 'a' <= alpha <= 'z':
			alpha = chr(ord(alpha) - 32)
		print("{}".format(alpha), end='')
	print()
	