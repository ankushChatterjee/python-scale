"""Tests for test module 1495 — covers src modules [5977, 5978, 5979, 5980]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5977 import add_5977
from module_5978 import subtract_5978
from module_5979 import multiply_5979
from module_5980 import divide_5980

def test_add_5977():
    assert add_5977(2, 3) == 5

def test_subtract_5978():
    assert subtract_5978(10, 4) == 6

def test_multiply_5979():
    assert multiply_5979(3, 7) == 21

def test_divide_5980():
    assert divide_5980(10, 2) == 5.0
