from Collatz import Collatz
import unittest

myCollatz = Collatz(6000)

# Test values are taken frm: https://www.dcode.fr/collatz-conjecture

class checkAndAnalyse(unittest.TestCase):
    def test_check(self):
        self.assertEqual(myCollatz.check(5), (True, 5))
        self.assertEqual(myCollatz.check(22), (True, 15))
        self.assertEqual(myCollatz.check(49), (True, 24))
        self.assertEqual(myCollatz.check(854), (True, 54))
        self.assertEqual(myCollatz.check(526), (True, 79))
        self.assertEqual(myCollatz.check(911), (True, 41))
    def test_analyse(self):
        self.assertDictEqual(myCollatz.analyse(5), { "isCollatz": True, "steps": 5, "moves": [5, 16, 8, 4, 2, 1], "maxReached": (16, 1), "evenSteps": 4, "oddSteps": 1})
        self.assertDictEqual(myCollatz.analyse(22), { "isCollatz": True, "steps": 15, "moves": [22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1], "maxReached": (52, 4), "evenSteps": 11, "oddSteps": 4})
        self.assertDictEqual(myCollatz.analyse(49), { "isCollatz": True, "steps": 24, "moves": [49, 148, 74, 37, 112, 56, 28, 14, 7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1], "maxReached": (148, 1), "evenSteps": 17, "oddSteps": 7})
        self.assertDictEqual(myCollatz.analyse(526), { "isCollatz": True, "steps": 79, "moves": [526, 263, 790, 395, 1186, 593, 1780, 890, 445, 1336, 668, 334, 167, 502, 251, 754, 377, 1132, 566, 283, 850, 425, 1276, 638, 319, 958, 479, 1438, 719, 2158, 1079, 3238, 1619, 4858, 2429, 7288, 3644, 1822, 911, 2734, 1367, 4102, 2051, 6154, 3077, 9232, 4616, 2308, 1154, 577, 1732, 866, 433, 1300, 650, 325, 976, 488, 244, 122, 61, 184, 92, 46, 23, 70, 35, 106, 53, 160, 80, 40, 20, 10, 5, 16, 8, 4, 2, 1], "maxReached": (9232, 45), "evenSteps": 52, "oddSteps": 27})

class checkUntilAndAnalyseUntil(unittest.TestCase):
    def test_checkUntil(self):
        # all tests should pass as this was previously tried and proven true until at least 2^68
        self.assertEqual(myCollatz.checkUntil(1), (True, -1))
        self.assertEqual(myCollatz.checkUntil(2), (True, -1))
        self.assertEqual(myCollatz.checkUntil(10), (True, -1))
        self.assertEqual(myCollatz.checkUntil(100), (True, -1))
        self.assertEqual(myCollatz.checkUntil(4324), (True, -1))
        self.assertEqual(myCollatz.checkUntil(45235), (True, -1))
        self.assertEqual(myCollatz.checkUntil(12472), (True, -1))
    def test_analyseUntil(self):
        self.assertDictEqual(myCollatz.analyseUntil(5), {'areCollatz': True, 'maxSteps': (7, 3), 'maxStepsNumbers': {0: [1], 1: [2], 2: [4], 5: [5], 7: [3]}, 'maxReached': (16, 5), 'maxReachedNumbers': {1: [1], 2: [2], 4: [4], 16: [3, 5]}})
        self.assertDictEqual(myCollatz.analyseUntil(10), {'areCollatz': True, 'maxSteps': (19, 9), 'maxStepsNumbers': {0: [1], 1: [2], 2: [4], 3: [8], 5: [5], 6: [10], 7: [3], 8: [6], 16: [7], 19: [9]}, 'maxReached': (52, 9), 'maxReachedNumbers': {1: [1], 2: [2], 4: [4], 8: [8], 16: [3, 5, 6, 10], 52: [7, 9]}})
        self.assertDictEqual(myCollatz.analyseUntil(15), {'areCollatz': True, 'maxSteps': (19, 9), 'maxStepsNumbers': {0: [1], 1: [2], 2: [4], 3: [8], 5: [5], 6: [10], 7: [3], 8: [6], 9: [12, 13], 14: [11], 16: [7], 17: [14, 15], 19: [9]}, 'maxReached': (160, 15), 'maxReachedNumbers':  {1: [1], 2: [2], 4: [4], 8: [8], 16: [3, 5, 6, 10, 12], 40: [13], 52: [7, 9, 11, 14], 160: [15]}})

if __name__ == '__main__':
    unittest.main()