"""Tests for test module 1333 — covers src modules [5329, 5330, 5331, 5332]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5329 import add_5329
from module_5330 import subtract_5330
from module_5331 import multiply_5331
from module_5332 import divide_5332

def test_add_5329():
    assert add_5329(2, 3) == 5

def test_subtract_5330():
    assert subtract_5330(10, 4) == 6

def test_multiply_5331():
    assert multiply_5331(3, 7) == 21

def test_divide_5332():
    assert divide_5332(10, 2) == 5.0
