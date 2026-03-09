"""Tests for test module 833 — covers src modules [3329, 3330, 3331, 3332]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3329 import add_3329
from module_3330 import subtract_3330
from module_3331 import multiply_3331
from module_3332 import divide_3332

def test_add_3329():
    assert add_3329(2, 3) == 5

def test_subtract_3330():
    assert subtract_3330(10, 4) == 6

def test_multiply_3331():
    assert multiply_3331(3, 7) == 21

def test_divide_3332():
    assert divide_3332(10, 2) == 5.0
