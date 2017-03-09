import unittest


class KenTest(unittest.TestCase):
    def test_something(self):
        self.assertIsInstance(1, int)

    def test_1(self):
        euler = __import__('1')
        self.assertIsInstance(euler.main(), int)

    def test_2(self):
        euler = __import__('2')
        self.assertIsInstance(euler.main(), int)


if __name__ == '__main__':
    unittest.main()