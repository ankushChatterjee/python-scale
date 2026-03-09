"""Tests for test module 7 — covers src modules [25, 26, 27, 28]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_25 import add_25
from module_26 import subtract_26
from module_27 import multiply_27
from module_28 import divide_28

def test_add_25():
    assert add_25(2, 3) == 5

def test_subtract_26():
    assert subtract_26(10, 4) == 6

def test_multiply_27():
    assert multiply_27(3, 7) == 21

def test_divide_28():
    assert divide_28(10, 2) == 5.0
