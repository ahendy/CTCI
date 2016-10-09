
class QueueStack():

    def __init__(self):
        self.s1 = []
        self.s2 = []

    def __eq__(self, val):
        return self.s1 == val
    
    def __str__(self):
        return str(self.s1)

    def is_empty(self):
        return len(s1)==0 and len(s2)==0

    def peek(self):
        if self.is_empty():
            raise Exception, "Fail"
        
        return s1[-1]

    def pop(self):
       
        while len(self.s1)>0:
            v = self.s1.pop()
            self.s2.append(v)
        # s2 has stack in reverse

        return self.s2.pop()

    def push(self, val):
        self.s1.append(val)
    


if __name__ == '__main__':
    q = QueueStack()
    q.push(5)
    q.push(4)
    q.push(3)

    print q
    assert q.pop() == 5
    assert q.pop() == 4
    assert q.pop() == 3


