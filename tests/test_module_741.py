"""Tests for test module 741 — covers src modules [2961, 2962, 2963, 2964]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2961 import add_2961
from module_2962 import subtract_2962
from module_2963 import multiply_2963
from module_2964 import divide_2964

def test_add_2961():
    assert add_2961(2, 3) == 5

def test_subtract_2962():
    assert subtract_2962(10, 4) == 6

def test_multiply_2963():
    assert multiply_2963(3, 7) == 21

def test_divide_2964():
    assert divide_2964(10, 2) == 5.0
