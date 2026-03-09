"""Tests for test module 1213 — covers src modules [4849, 4850, 4851, 4852]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4849 import add_4849
from module_4850 import subtract_4850
from module_4851 import multiply_4851
from module_4852 import divide_4852

def test_add_4849():
    assert add_4849(2, 3) == 5

def test_subtract_4850():
    assert subtract_4850(10, 4) == 6

def test_multiply_4851():
    assert multiply_4851(3, 7) == 21

def test_divide_4852():
    assert divide_4852(10, 2) == 5.0
