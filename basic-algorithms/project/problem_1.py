import unittest
import math

def get_approximation(x, b):
    return (x + b/x)*.5

def get_delta(old_guess, new_guess):
    return math.fabs(old_guess - new_guess)

def sqrt(number):
    if number == 0 or number == 1:
        return number
    guess = number//2
    while True:
        new_guess = get_approximation(guess, number)
        if get_delta(guess, new_guess) < .1:
            break
        guess = new_guess
    return math.floor(new_guess)


class Tests(unittest.TestCase):

    def test_0(self):
        self.assertEqual(sqrt(9),3)
    def test_1(self):
        self.assertEqual(sqrt(1),1)
    def test_2(self):
        self.assertEqual(sqrt(0),0)
    def test_3(self):
        self.assertEqual(sqrt(16),4)
    def test_4(self):
        self.assertEqual(sqrt(27),5)
    def test_5(self):
        self.assertEqual(sqrt(25),5)
    def test_6(self):
        self.assertEqual(sqrt(26),5)
    def test_7(self):
        self.assertEqual(sqrt(100),10)
    def test_8(self):
        self.assertEqual(sqrt(82),9)

if __name__ == '__main__':
    unittest.main()