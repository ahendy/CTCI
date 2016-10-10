from tree import *

def is_balanced(tree):
	"""balanced if left and right tree differ by at most 1"""

	def get_height(tree):
		if not tree:
			return 0
		
		lheight = get_height(tree.left)
		rheight = get_height(tree.right)
		if lheight == -1 or rheight == -1:
			return -1

		diff = abs(lheight - rheight)
		if diff > 1:
			return -1
		else:
			return max(lheight, rheight) + 1

	return False if get_height(tree) == -1 else True

if __name__ == '__main__':
	tree = make_tree(range(10))

	assert is_balanced(tree) == True
	tree.left = None
	assert is_balanced(tree) == False
