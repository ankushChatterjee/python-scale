"""Tests for test module 1221 — covers src modules [4881, 4882, 4883, 4884]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4881 import add_4881
from module_4882 import subtract_4882
from module_4883 import multiply_4883
from module_4884 import divide_4884

def test_add_4881():
    assert add_4881(2, 3) == 5

def test_subtract_4882():
    assert subtract_4882(10, 4) == 6

def test_multiply_4883():
    assert multiply_4883(3, 7) == 21

def test_divide_4884():
    assert divide_4884(10, 2) == 5.0
