import unittest
from unittest import mock
from unittest.mock import mock_open, patch, MagicMock

from assertpy import *

from sample.file import File

class TestFile(unittest.TestCase):

    @patch('builtins.open', mock_open(read_data='gitara'))
    def test_read(self):
        read_func = File().read('plik.txt')
        assert_that(read_func).is_equal_to('gitara')

    def test_write(self):
        open = mock_open(read_data='gitara')

        with patch('builtins.open', open):
            File().write('plik.txt', 'tekst')

        open.assert_called_once_with('plik.txt', 'w')

    def test_del(self):
        with patch('os.remove'):
            File().delete('data/data_file')

    def test_del_exeption(self):
        with patch('os.remove'):
            assert_that(File().delete).raises(Exception).when_called_with('foo')


if __name__ == '__main__':
    unittest.main()
