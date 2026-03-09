"""Tests for test module 759 — covers src modules [3033, 3034, 3035, 3036]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3033 import add_3033
from module_3034 import subtract_3034
from module_3035 import multiply_3035
from module_3036 import divide_3036

def test_add_3033():
    assert add_3033(2, 3) == 5

def test_subtract_3034():
    assert subtract_3034(10, 4) == 6

def test_multiply_3035():
    assert multiply_3035(3, 7) == 21

def test_divide_3036():
    assert divide_3036(10, 2) == 5.0
