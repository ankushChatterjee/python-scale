"""Tests for test module 15 — covers src modules [57, 58, 59, 60]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_57 import add_57
from module_58 import subtract_58
from module_59 import multiply_59
from module_60 import divide_60

def test_add_57():
    assert add_57(2, 3) == 5

def test_subtract_58():
    assert subtract_58(10, 4) == 6

def test_multiply_59():
    assert multiply_59(3, 7) == 21

def test_divide_60():
    assert divide_60(10, 2) == 5.0
