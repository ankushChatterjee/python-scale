"""Tests for test module 465 — covers src modules [1857, 1858, 1859, 1860]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1857 import add_1857
from module_1858 import subtract_1858
from module_1859 import multiply_1859
from module_1860 import divide_1860

def test_add_1857():
    assert add_1857(2, 3) == 5

def test_subtract_1858():
    assert subtract_1858(10, 4) == 6

def test_multiply_1859():
    assert multiply_1859(3, 7) == 21

def test_divide_1860():
    assert divide_1860(10, 2) == 5.0
