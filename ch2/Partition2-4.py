from LL import *

def partition(partition, head):
	tail = curr = head
	# while tail.next:
		# tail = tail.next

	while curr:
		next = curr.next
		# curr.next = None
		if curr.val < partition:
			curr.next = head
			head = curr

		else:
			tail.next = curr
			tail = curr 

		curr = next

	tail.next = None
	return head

if __name__ == '__main__':
	head = make_LL([3,5,8,5,10,2,1])
	head = partition(5, head)
	printl(head)

	seen = False
	for v in make_list(head):
		if v == partition:
			seen = True

		if v < partition and seen:
			assert False
	assert True
	print "Test 1 passed."
