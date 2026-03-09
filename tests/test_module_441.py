"""Tests for test module 441 — covers src modules [1761, 1762, 1763, 1764]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1761 import add_1761
from module_1762 import subtract_1762
from module_1763 import multiply_1763
from module_1764 import divide_1764

def test_add_1761():
    assert add_1761(2, 3) == 5

def test_subtract_1762():
    assert subtract_1762(10, 4) == 6

def test_multiply_1763():
    assert multiply_1763(3, 7) == 21

def test_divide_1764():
    assert divide_1764(10, 2) == 5.0
