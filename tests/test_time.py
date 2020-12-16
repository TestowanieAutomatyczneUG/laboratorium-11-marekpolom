import unittest
from unittest.mock import *

import sample.time as time


class TestTime(unittest.TestCase):

    def test_time(self):
        #mock
        test_object = time.Checker()
        test_object.time.getTime = MagicMock(return_value = 18)

        #test
        test_object.reminder('file')
        self.assertTrue(test_object.time.filePlayed)

    def test_time_1(self):
        #mock
        test_object = time.Checker()
        test_object.time.getTime = MagicMock(return_value = 15)

        #test
        test_object.reminder('file')
        self.assertFalse(test_object.time.filePlayed)


if __name__ == '__main__':
    unittest.main()
