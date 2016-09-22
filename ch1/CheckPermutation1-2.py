
def check_perm(str1, str2):
	"""O(nlogn) runtime"""
	return sorted(str1) == sorted(str2)



if __name__ == '__main__':
	assert check_perm("aba", "baa") == True