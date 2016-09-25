from LL import *

def is_palindrome(head):

	slo = fast = head
	stack = []
	while fast and fast.next:
		stack.append(slo.val)
		slo = slo.next
		fast = fast.next.next
	
	# slow now at middle
	if fast:
		slo = slo.next # odd case
	
	while slo:
		curr = stack.pop()

		if slo.val != curr:
			return False
		slo = slo.next

	return True

if __name__ == '__main__':
	head = make_LL([1,2,3,2,1])
	assert is_palindrome(head) == True
	print "Passed Test 1."
	head = make_LL([1,2,3,5,3,2,1])
	assert is_palindrome(head) == True
	print "Passed Test 2."