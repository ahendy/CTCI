from LinkedList import *
from tree import *


def depth_tree(tree):

	sol = []
	latest = {}

	def recurse(sol, latest, root, depth):
		if not root:
			return

		if len(sol) == depth:
			sol.append(Node(root.val))
			latest[depth] = sol[depth]
		else:
			latest[depth].next = Node(root.val)
			latest[depth] = latest[depth].next

		recurse(sol, latest,root.left, depth+1)
		recurse(sol, latest,root.right, depth+1)

	recurse(sol, latest, tree, 0)
	return sol

if __name__ == '__main__':
	tree = make_tree(range(10))
	res = depth_tree(tree)

