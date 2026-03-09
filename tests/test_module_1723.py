"""Tests for test module 1723 — covers src modules [6889, 6890, 6891, 6892]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6889 import add_6889
from module_6890 import subtract_6890
from module_6891 import multiply_6891
from module_6892 import divide_6892

def test_add_6889():
    assert add_6889(2, 3) == 5

def test_subtract_6890():
    assert subtract_6890(10, 4) == 6

def test_multiply_6891():
    assert multiply_6891(3, 7) == 21

def test_divide_6892():
    assert divide_6892(10, 2) == 5.0
