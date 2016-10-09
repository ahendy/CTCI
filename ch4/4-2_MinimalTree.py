from tree import *

def min_tree(nodes):
	"""in: sorted list"""
	"""out: minimum height bst"""

	def recurse(l, r, nodes):
		if l > r:
			return 
		
		m = (l+r) / 2
		treenode = TreeNode(nodes[m])
		treenode.left = recurse(l, m-1, nodes)
		treenode.right = recurse(m+1, r, nodes)

		return treenode

	root = recurse(0, len(nodes)-1, nodes)

	return root


if __name__ == '__main__':
	
	nodes = range(10)
	assert min_tree(nodes) == [
				[4],
				[1,7],
				[0,	2, 5, 8],	
				[3, 6, 9],
	]

	