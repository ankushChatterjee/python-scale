"""Tests for test module 713 — covers src modules [2849, 2850, 2851, 2852]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2849 import add_2849
from module_2850 import subtract_2850
from module_2851 import multiply_2851
from module_2852 import divide_2852

def test_add_2849():
    assert add_2849(2, 3) == 5

def test_subtract_2850():
    assert subtract_2850(10, 4) == 6

def test_multiply_2851():
    assert multiply_2851(3, 7) == 21

def test_divide_2852():
    assert divide_2852(10, 2) == 5.0
