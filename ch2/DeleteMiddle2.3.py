from LL import *

def delete_node(node):
	nxtnxt = node.next.next
	node.val = node.next.val
	node.next = nxtnxt

if __name__ == '__main__':
	head = make_LL([0,1,2,3,4])
	to_del = head.next	
	delete_node(to_del)

	assert make_list(head) == [0,2,3,4]