
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

if __name__ == '__main__':
    head = Node(1)
    head.append(6)

    assert head.val == 1
    print "Test 1 passed."
    assert head.next.val == 6
    print "Test 2 passed."