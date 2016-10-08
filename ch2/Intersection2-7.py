from LL import *

def intersects(l1, l2):
    
    if not l1 or not l2:
        return False
    
    len1, len2 = length(l1), length(l2)
    short, lng =  len1, len2

    # Get longer length
    if len1 > len2:
        short = l2
        lng = l1

    dif = abs(len1 - len2)
    count = 0
    # move ptrs till equal length till end of lists
    while lng and count < dif:
        lng = lng.next
        count += 1

    while lng:
        if lng is short:
            return True
        
        lng = lng.next
        short = short.next

    return False

if __name__ == '__main__':
    intersect_node = make_LL([5,4,3,2,1])
    l1 = make_LL([55])
    l2 = make_LL([44])

    l2.next = intersect_node
    l1.next = intersect_node

    tests = (
        ((l1,l2), True),
        ((l2, Node(5)), False),
    )

    for i, (param, sol) in enumerate(tests):
        assert intersects(*param) == sol
        print "Passed Test %d." % (i, )
