import unittest

def min_operations(target):
    """
    Return number of steps taken to reach a target number
    input:- target number an integer
    output:- number of steps an integer
    """
    num_steps = 0
    
    # start backwards from the target
    # if target is odd --> subtract 1
    # if target is even --> divide by 2
    while target != 0:
        if target % 2 == 0:
            target = target // 2

        else:
            target = target - 1
        num_steps += 1
    return num_steps
    

class Tests(unittest.TestCase):

    def test_1(self):
        target = 18
        solution = 6
        self.assertEqual(solution, min_operations(target))

    def test_2(self):
        target = 69
        solution = 9
        self.assertEqual(solution, min_operations(target))

if __name__ == '__main__':
    unittest.main()