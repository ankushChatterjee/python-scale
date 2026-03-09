"""Tests for test module 2213 — covers src modules [8849, 8850, 8851, 8852]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8849 import add_8849
from module_8850 import subtract_8850
from module_8851 import multiply_8851
from module_8852 import divide_8852

def test_add_8849():
    assert add_8849(2, 3) == 5

def test_subtract_8850():
    assert subtract_8850(10, 4) == 6

def test_multiply_8851():
    assert multiply_8851(3, 7) == 21

def test_divide_8852():
    assert divide_8852(10, 2) == 5.0
