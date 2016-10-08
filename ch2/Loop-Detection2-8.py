from LL import *

def find_loop(head):
    
    fast = slow = head

    while fast and fast.next and fast is not slow:
        fast = fast.next.next
        slow = slow.next

    # fast == slow now
    # from beginnning loop till equal
    slow = head
    while fast is not slow:
        fast = fast.next
        slow = slow.next

    return slow


if __name__ == '__main__':
    l1 = make_LL([1,2,3])
    head = Node(5)
    head.next = l1
    l1.append(head)

    tests = (
        (head, head),
    )

    for i, (param, sol) in enumerate(tests):
        assert find_loop(param) == sol
        print "Passed Test %d." % (i, )

