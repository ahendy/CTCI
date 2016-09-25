from itertools import izip

def is_rotation(s1, s2):
    """Decide if s2 is a rotation of s1"""
    """does there exist a x,y such that xy = s1 and yx = s2? """
    """Time O(N), space O(N)""" 
    return len(s1) == len(s2) and ("".join(2*[s1])).find(s2) != -1


if __name__ == '__main__':
    assert is_rotation("waterbottle", "erbottlewat") == True
    print "Test 1 passed."