
class SortStack():

    def __init__(self):
        self.s1 = []
        self.s2 = []

    def __str__(self):
        return str(self.s1)

    def __eq__(self, v):
        return self.s1 == v

    def empty(self):
        return not len(self.s1) > 0

    def peek(self):
        if self.empty():
            raise Exception, "Fail"

        return self.s1[-1]

    def push(self, val):
        
        while not self.empty() and self.peek() > val:
            v = self.s1.pop()
            self.s2.append(v)

        self.s1.append(val)
        
        while len(self.s2) > 0:
            v = self.s2.pop()
            self.s1.append(v)

    def pop(self):
        if self.empty():
            raise Exception, "Fail"

        return self.s1.pop()

if __name__ == '__main__':

    stack = SortStack()
    stack.push(5)
    stack.push(3)
    stack.push(4)
    assert [3,4,5] == stack
    print "test 1 passed"

    import random
    stack2,tester = SortStack(), []

    for _ in range(1000):
        rand = random.randint(1, 1000)
        tester.append(rand)
        stack2.push(rand)

    assert sorted(tester) == stack2
    print "test 2 passed"






