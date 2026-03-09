"""Tests for test module 1833 — covers src modules [7329, 7330, 7331, 7332]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7329 import add_7329
from module_7330 import subtract_7330
from module_7331 import multiply_7331
from module_7332 import divide_7332

def test_add_7329():
    assert add_7329(2, 3) == 5

def test_subtract_7330():
    assert subtract_7330(10, 4) == 6

def test_multiply_7331():
    assert multiply_7331(3, 7) == 21

def test_divide_7332():
    assert divide_7332(10, 2) == 5.0
