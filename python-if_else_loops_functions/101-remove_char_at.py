#!/usr/bin/python3
def remove_char_at(str, n):
	new = ""
	for i in range(len(str)):
		if i == n:
			continue
		else:
			new += str[i]
	return new
