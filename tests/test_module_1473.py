"""Tests for test module 1473 — covers src modules [5889, 5890, 5891, 5892]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5889 import add_5889
from module_5890 import subtract_5890
from module_5891 import multiply_5891
from module_5892 import divide_5892

def test_add_5889():
    assert add_5889(2, 3) == 5

def test_subtract_5890():
    assert subtract_5890(10, 4) == 6

def test_multiply_5891():
    assert multiply_5891(3, 7) == 21

def test_divide_5892():
    assert divide_5892(10, 2) == 5.0
