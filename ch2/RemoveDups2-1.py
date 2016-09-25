from LL import * 

def remove_dups(head):
    seen = set()
    prev = None
    front = head

    while head:
        if head.val in seen:
            prev.next = head.next
        else:
            seen.add(head.val)
            prev = head
            
        head = head.next

    return front
if __name__ == '__main__':

    head = make_LL([1,1,2,2,3,3,1,1])
    remove_dups(head)    
    assert make_list(head) == [1,2,3]
    print "Test 1 passed."