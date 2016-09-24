from itertools import izip

def is_add(str1, str2):
	num_diff = 0
	n = len(str1)
	m = len(str2)
	offset = 0
	for i in xrange(n):
		l = i + offset
		if str1[i] != str2[l]:
			offset += 1

	return offset == 1 or (offset == 0 if n==m else (offset>0))

def one_away(str1, str2):
	if len(str1) > len(str2):
		return	is_add(str2, str1)
	elif len(str2) < len(str1):
		return is_add(str1, str2)
	else:
		return is_add(str1, str2)

if __name__ == '__main__':
	assert one_away("pale", "ple") == True
	assert one_away("pales", "pale") == True
	assert one_away("pale", "bale") == True
	assert one_away("bake", "pale") == False
