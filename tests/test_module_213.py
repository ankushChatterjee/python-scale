"""Tests for test module 213 — covers src modules [849, 850, 851, 852]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_849 import add_849
from module_850 import subtract_850
from module_851 import multiply_851
from module_852 import divide_852

def test_add_849():
    assert add_849(2, 3) == 5

def test_subtract_850():
    assert subtract_850(10, 4) == 6

def test_multiply_851():
    assert multiply_851(3, 7) == 21

def test_divide_852():
    assert divide_852(10, 2) == 5.0
