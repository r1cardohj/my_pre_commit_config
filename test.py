import unittest

from core import add_one, sub_one


class TestAddOneAndSubOne(unittest.TestCase):
    def test_add_one(self):
        self.assertEqual(add_one(1), 2)

    def test_sub_one(self):
        self.assertEqual(sub_one(1), 0)


if __name__ == '__main__':
    unittest.main()
