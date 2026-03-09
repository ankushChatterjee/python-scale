"""Tests for test module 495 — covers src modules [1977, 1978, 1979, 1980]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1977 import add_1977
from module_1978 import subtract_1978
from module_1979 import multiply_1979
from module_1980 import divide_1980

def test_add_1977():
    assert add_1977(2, 3) == 5

def test_subtract_1978():
    assert subtract_1978(10, 4) == 6

def test_multiply_1979():
    assert multiply_1979(3, 7) == 21

def test_divide_1980():
    assert divide_1980(10, 2) == 5.0
