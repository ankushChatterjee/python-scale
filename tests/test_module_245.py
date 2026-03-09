"""Tests for test module 245 — covers src modules [977, 978, 979, 980]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_977 import add_977
from module_978 import subtract_978
from module_979 import multiply_979
from module_980 import divide_980

def test_add_977():
    assert add_977(2, 3) == 5

def test_subtract_978():
    assert subtract_978(10, 4) == 6

def test_multiply_979():
    assert multiply_979(3, 7) == 21

def test_divide_980():
    assert divide_980(10, 2) == 5.0
