"""Tests for test module 473 — covers src modules [1889, 1890, 1891, 1892]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1889 import add_1889
from module_1890 import subtract_1890
from module_1891 import multiply_1891
from module_1892 import divide_1892

def test_add_1889():
    assert add_1889(2, 3) == 5

def test_subtract_1890():
    assert subtract_1890(10, 4) == 6

def test_multiply_1891():
    assert multiply_1891(3, 7) == 21

def test_divide_1892():
    assert divide_1892(10, 2) == 5.0
