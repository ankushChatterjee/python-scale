"""Tests for test module 963 — covers src modules [3849, 3850, 3851, 3852]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3849 import add_3849
from module_3850 import subtract_3850
from module_3851 import multiply_3851
from module_3852 import divide_3852

def test_add_3849():
    assert add_3849(2, 3) == 5

def test_subtract_3850():
    assert subtract_3850(10, 4) == 6

def test_multiply_3851():
    assert multiply_3851(3, 7) == 21

def test_divide_3852():
    assert divide_3852(10, 2) == 5.0
