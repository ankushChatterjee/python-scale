"""Tests for test module 965 — covers src modules [3857, 3858, 3859, 3860]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3857 import add_3857
from module_3858 import subtract_3858
from module_3859 import multiply_3859
from module_3860 import divide_3860

def test_add_3857():
    assert add_3857(2, 3) == 5

def test_subtract_3858():
    assert subtract_3858(10, 4) == 6

def test_multiply_3859():
    assert multiply_3859(3, 7) == 21

def test_divide_3860():
    assert divide_3860(10, 2) == 5.0
