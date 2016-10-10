from tree import *
import sys

def is_valid(tree, min_=None, max_=None):
	if not tree:
		return True

	if (min_ and tree.val <= min_) or (max_ and tree.val >= max_):
		return False

	return is_valid(tree.left, min_, tree.val) and is_valid(tree.right, tree.val, max_)

if __name__ == '__main__':
	tree = TreeNode(5)
	tree.left = TreeNode(3)
	tree.right = TreeNode(7)

	assert is_valid(tree) == True
	tree.left.right = TreeNode(8)
	assert is_valid(tree) == False