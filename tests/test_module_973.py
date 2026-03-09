"""Tests for test module 973 — covers src modules [3889, 3890, 3891, 3892]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3889 import add_3889
from module_3890 import subtract_3890
from module_3891 import multiply_3891
from module_3892 import divide_3892

def test_add_3889():
    assert add_3889(2, 3) == 5

def test_subtract_3890():
    assert subtract_3890(10, 4) == 6

def test_multiply_3891():
    assert multiply_3891(3, 7) == 21

def test_divide_3892():
    assert divide_3892(10, 2) == 5.0
