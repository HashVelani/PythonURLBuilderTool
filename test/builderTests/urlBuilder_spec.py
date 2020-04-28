import unittest
from builders import urlBuilder

class urlBuilderSpec(unittest.TestCase):
    def test_hello(self):
        self.assertEqual(urlBuilder(), 'hello world')

if __name__ == '__main__':
    unittest.main()