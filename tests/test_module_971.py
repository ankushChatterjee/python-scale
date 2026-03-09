"""Tests for test module 971 — covers src modules [3881, 3882, 3883, 3884]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3881 import add_3881
from module_3882 import subtract_3882
from module_3883 import multiply_3883
from module_3884 import divide_3884

def test_add_3881():
    assert add_3881(2, 3) == 5

def test_subtract_3882():
    assert subtract_3882(10, 4) == 6

def test_multiply_3883():
    assert multiply_3883(3, 7) == 21

def test_divide_3884():
    assert divide_3884(10, 2) == 5.0
