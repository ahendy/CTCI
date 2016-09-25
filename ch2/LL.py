
class Node():
    def __init__(self, val):
        self.val = val
        self.next = None


    def append(self, val):
        if type(val)!=Node:
            val = Node(val)
            head = self

        while head.next != None:
            head = head.next

        head.next = val

def make_LL(nodes=[1,3,5,4,2]):

    head = None
    for val in nodes:
        if head is None:
            head = Node(val)
        else:
            head.append(val)

    return head

def printl(head):

    while head:
        print head.val
        head = head.next

def make_list(head):
    l = []

    while head is not None:
        l.append(head.val)
        head = head.next
    return l

def length(head, length_=0):
    return 1 + length(head.next, length_) if head else 0

if __name__ == '__main__':
    head = Node(1)
    head.append(6)

    assert head.val == 1
    print "Test 1 passed."
    assert head.next.val == 6
    print "Test 2 passed."
    assert make_list(make_LL()) == [1,3,5,4,2]
    print "Test 3 passed."
    assert length(make_LL(range(10))) == 10
    print "Test 4 passed."