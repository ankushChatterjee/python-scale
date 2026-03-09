"""Tests for test module 2157 — covers src modules [8625, 8626, 8627, 8628]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8625 import add_8625
from module_8626 import subtract_8626
from module_8627 import multiply_8627
from module_8628 import divide_8628

def test_add_8625():
    assert add_8625(2, 3) == 5

def test_subtract_8626():
    assert subtract_8626(10, 4) == 6

def test_multiply_8627():
    assert multiply_8627(3, 7) == 21

def test_divide_8628():
    assert divide_8628(10, 2) == 5.0
