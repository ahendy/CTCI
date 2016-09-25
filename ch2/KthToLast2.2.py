from LL import *

def kth_last_element(k, head):
	"Uses length of list. Requires two passes O(n)"
	len_ = length(head)
	count = 0

	while len_-count != k:
		head = head.next
		count += 1
	return head.val

def kth_last_element2(k, head):
	"""Move hare k steps ahead, make head catch up,
	once hare is None head is now at n-k. 1 pass O(n)"""
 	hare = head
	for _ in xrange(k):
		hare = hare.next

	while hare:
		hare = hare.next
		head = head.next

	return head.val

if __name__ == '__main__':
	head = make_LL([1,2,3,4,5,6])
	assert kth_last_element(3, head) == 4
	print "Passed Test 1."
	assert kth_last_element2(3, head) == 4
	print "Passed Test 2."
