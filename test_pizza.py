import unittest
from unittest.mock import patch, ANY
from decorators import log
from test_utils import create_fake_timer


class TestLog(unittest.TestCase):

    @patch('time.perf_counter', create_fake_timer())
    def test_proper_delta(self):
        """Правильно считается дельта по времени"""
        with patch('print') as m:
            log(lambda: ())()

        m.assert_called_once_with(ANY, '2.000')

    def test_func_with_exception(self):
        with self.assertRaises(IndexError):
            log(lambda: [][0])()



