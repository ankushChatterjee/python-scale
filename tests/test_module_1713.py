"""Tests for test module 1713 — covers src modules [6849, 6850, 6851, 6852]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6849 import add_6849
from module_6850 import subtract_6850
from module_6851 import multiply_6851
from module_6852 import divide_6852

def test_add_6849():
    assert add_6849(2, 3) == 5

def test_subtract_6850():
    assert subtract_6850(10, 4) == 6

def test_multiply_6851():
    assert multiply_6851(3, 7) == 21

def test_divide_6852():
    assert divide_6852(10, 2) == 5.0
