"""Tests for test module 1441 — covers src modules [5761, 5762, 5763, 5764]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5761 import add_5761
from module_5762 import subtract_5762
from module_5763 import multiply_5763
from module_5764 import divide_5764

def test_add_5761():
    assert add_5761(2, 3) == 5

def test_subtract_5762():
    assert subtract_5762(10, 4) == 6

def test_multiply_5763():
    assert multiply_5763(3, 7) == 21

def test_divide_5764():
    assert divide_5764(10, 2) == 5.0
