"""Tests for test module 1365 — covers src modules [5457, 5458, 5459, 5460]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5457 import add_5457
from module_5458 import subtract_5458
from module_5459 import multiply_5459
from module_5460 import divide_5460

def test_add_5457():
    assert add_5457(2, 3) == 5

def test_subtract_5458():
    assert subtract_5458(10, 4) == 6

def test_multiply_5459():
    assert multiply_5459(3, 7) == 21

def test_divide_5460():
    assert divide_5460(10, 2) == 5.0
