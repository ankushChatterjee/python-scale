"""Tests for test module 715 — covers src modules [2857, 2858, 2859, 2860]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2857 import add_2857
from module_2858 import subtract_2858
from module_2859 import multiply_2859
from module_2860 import divide_2860

def test_add_2857():
    assert add_2857(2, 3) == 5

def test_subtract_2858():
    assert subtract_2858(10, 4) == 6

def test_multiply_2859():
    assert multiply_2859(3, 7) == 21

def test_divide_2860():
    assert divide_2860(10, 2) == 5.0
