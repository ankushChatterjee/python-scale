"""Tests for test module 2113 — covers src modules [8449, 8450, 8451, 8452]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8449 import add_8449
from module_8450 import subtract_8450
from module_8451 import multiply_8451
from module_8452 import divide_8452

def test_add_8449():
    assert add_8449(2, 3) == 5

def test_subtract_8450():
    assert subtract_8450(10, 4) == 6

def test_multiply_8451():
    assert multiply_8451(3, 7) == 21

def test_divide_8452():
    assert divide_8452(10, 2) == 5.0
