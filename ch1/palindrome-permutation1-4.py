from collections import Counter

def is_permutation(words):

	# words = "#" + "#".join("".join(words.lower().split())) + "#"
 	words = "".join(words.lower().split())
 	c = Counter(words)	
 	num_singles = 0
	for word, count in c.iteritems():
		if count == 1:
			
			if num_singles > 0:
				return False
			else:
				num_singles += 1
		
		elif count % 2 > 0:
			return False

	return True

	
if __name__ == '__main__':
	assert is_permutation("Tact Coa") == True
	assert is_permutation("ffmmeg") == False
