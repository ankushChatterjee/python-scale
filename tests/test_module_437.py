"""Tests for test module 437 — covers src modules [1745, 1746, 1747, 1748]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1745 import add_1745
from module_1746 import subtract_1746
from module_1747 import multiply_1747
from module_1748 import divide_1748

def test_add_1745():
    assert add_1745(2, 3) == 5

def test_subtract_1746():
    assert subtract_1746(10, 4) == 6

def test_multiply_1747():
    assert multiply_1747(3, 7) == 21

def test_divide_1748():
    assert divide_1748(10, 2) == 5.0
