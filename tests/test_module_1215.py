"""Tests for test module 1215 — covers src modules [4857, 4858, 4859, 4860]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4857 import add_4857
from module_4858 import subtract_4858
from module_4859 import multiply_4859
from module_4860 import divide_4860

def test_add_4857():
    assert add_4857(2, 3) == 5

def test_subtract_4858():
    assert subtract_4858(10, 4) == 6

def test_multiply_4859():
    assert multiply_4859(3, 7) == 21

def test_divide_4860():
    assert divide_4860(10, 2) == 5.0
