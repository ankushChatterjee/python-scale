"""Tests for test module 991 — covers src modules [3961, 3962, 3963, 3964]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3961 import add_3961
from module_3962 import subtract_3962
from module_3963 import multiply_3963
from module_3964 import divide_3964

def test_add_3961():
    assert add_3961(2, 3) == 5

def test_subtract_3962():
    assert subtract_3962(10, 4) == 6

def test_multiply_3963():
    assert multiply_3963(3, 7) == 21

def test_divide_3964():
    assert divide_3964(10, 2) == 5.0
