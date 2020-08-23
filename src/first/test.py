import unittest

class TestFunc(unittest.TestCase):
    def test_func(self):
        from hellow import printMessage
        self.assertIsNone(printMessage('てすと'))
