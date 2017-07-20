import unittest
from app import hello

class HelloTestCase(unittest.TestCase):
    """Tests for simpleapp.py"""

    def test_is_output_hw(self):
        """Is the output of your Python App what you expect?"""
        self.assertTrue(hello() == "Dont do drugs kids.")

if __name__ == '__main__':
    unittest.main()