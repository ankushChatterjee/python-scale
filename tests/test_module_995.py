"""Tests for test module 995 — covers src modules [3977, 3978, 3979, 3980]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3977 import add_3977
from module_3978 import subtract_3978
from module_3979 import multiply_3979
from module_3980 import divide_3980

def test_add_3977():
    assert add_3977(2, 3) == 5

def test_subtract_3978():
    assert subtract_3978(10, 4) == 6

def test_multiply_3979():
    assert multiply_3979(3, 7) == 21

def test_divide_3980():
    assert divide_3980(10, 2) == 5.0
