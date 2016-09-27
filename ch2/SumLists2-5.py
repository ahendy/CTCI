from LL import *

def sum_(l1, l2):
    curr = sol = Node(-1)
    carry = None
    count = 0

    while l1 or l2 or carry != 0:
        l2val = 0 if l2 is None else l2.val
        l1val = 0 if l1 is None else l1.val
        carry = 0 if carry is None else carry 

        comb = l1val + l2val + carry
        res = comb % 10
        carry = comb/10 % 10
        curr.next = Node(res)

        l1 = l1.next if l1 else l1
        l2 = l2.next if l2 else l2
        
        curr = curr.next
        count += 1
    return sol.next 

if __name__ == '__main__':
    tests = [
        # (head1), (head2), (sol)
        ([7,1,6], [5,9,2], [2,1,9]),
        ([5], [5], [0,1]),

    ]
    
    for i, (h1, h2, sol) in enumerate(tests):
        h1 = make_LL(h1)
        h2 = make_LL(h2)
        res = sum_(h1, h2)
        assert make_list(res) == sol 
        print "Passed test %d." % (i,)