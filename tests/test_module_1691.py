"""Tests for test module 1691 — covers src modules [6761, 6762, 6763, 6764]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6761 import add_6761
from module_6762 import subtract_6762
from module_6763 import multiply_6763
from module_6764 import divide_6764

def test_add_6761():
    assert add_6761(2, 3) == 5

def test_subtract_6762():
    assert subtract_6762(10, 4) == 6

def test_multiply_6763():
    assert multiply_6763(3, 7) == 21

def test_divide_6764():
    assert divide_6764(10, 2) == 5.0
