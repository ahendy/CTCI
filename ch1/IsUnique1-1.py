
def is_unique1(word):
	"""O(n) space, O(n) runtime """
	visited = set()
	for ch in word:
		if ch in visited:
			return False
		visited.add(ch)

	return True

def is_unique2(word):
	"""Constant space, O(nlogn) runtime"""
	word = sorted(word)
	for i in xrange(1, len(word)-1):
		if word[i-1] == word[i] or word[i+1] == word[i]:
			return False

	return True

def is_unique3(word):
	"""Constant Space, O(n^2) runtime"""
	for i, ch in enumerate(word):
		for j in range(i+1, len(word)):
			if ch == word[j]:
				return False
	return True


if __name__ == '__main__':
	
	assert is_unique1("friend") == True
	assert is_unique2("friend") == True
	assert is_unique3("friend") == True

	assert is_unique1("aaa") == False
	assert is_unique2("aaa") == False
	assert is_unique3("aaa") == False