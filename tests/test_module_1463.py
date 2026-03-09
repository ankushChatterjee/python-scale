"""Tests for test module 1463 — covers src modules [5849, 5850, 5851, 5852]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5849 import add_5849
from module_5850 import subtract_5850
from module_5851 import multiply_5851
from module_5852 import divide_5852

def test_add_5849():
    assert add_5849(2, 3) == 5

def test_subtract_5850():
    assert subtract_5850(10, 4) == 6

def test_multiply_5851():
    assert multiply_5851(3, 7) == 21

def test_divide_5852():
    assert divide_5852(10, 2) == 5.0
