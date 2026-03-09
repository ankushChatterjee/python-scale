"""Tests for test module 1973 — covers src modules [7889, 7890, 7891, 7892]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7889 import add_7889
from module_7890 import subtract_7890
from module_7891 import multiply_7891
from module_7892 import divide_7892

def test_add_7889():
    assert add_7889(2, 3) == 5

def test_subtract_7890():
    assert subtract_7890(10, 4) == 6

def test_multiply_7891():
    assert multiply_7891(3, 7) == 21

def test_divide_7892():
    assert divide_7892(10, 2) == 5.0
