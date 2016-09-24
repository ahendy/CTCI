
def compress(string):
	if not string:
		return ""

	compressed = [string[0]]
	count = 1

	for i in range(1, len(string)):
		ch = string[i]
		if ch != compressed[-1]:
			compressed.append(str(count))
			compressed.append(ch)
			count = 1 
		elif i == len(string)-1:
			compressed.append(str(count+1))
		else:
			count += 1

	return min(string, "".join(compressed), key=len)

if __name__ == '__main__':
	assert compress("aabcccaaa") == "a2b1c3a3"
	assert compress("aaabbb") == "a3b3"
	assert compress("") == ""
	assert compress("abc") == "abc"
	assert compress("abbbbb") == "a1b5"
	