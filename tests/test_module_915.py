"""Tests for test module 915 — covers src modules [3657, 3658, 3659, 3660]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3657 import add_3657
from module_3658 import subtract_3658
from module_3659 import multiply_3659
from module_3660 import divide_3660

def test_add_3657():
    assert add_3657(2, 3) == 5

def test_subtract_3658():
    assert subtract_3658(10, 4) == 6

def test_multiply_3659():
    assert multiply_3659(3, 7) == 21

def test_divide_3660():
    assert divide_3660(10, 2) == 5.0
