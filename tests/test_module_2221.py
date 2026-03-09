"""Tests for test module 2221 — covers src modules [8881, 8882, 8883, 8884]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8881 import add_8881
from module_8882 import subtract_8882
from module_8883 import multiply_8883
from module_8884 import divide_8884

def test_add_8881():
    assert add_8881(2, 3) == 5

def test_subtract_8882():
    assert subtract_8882(10, 4) == 6

def test_multiply_8883():
    assert multiply_8883(3, 7) == 21

def test_divide_8884():
    assert divide_8884(10, 2) == 5.0
