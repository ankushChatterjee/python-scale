"""Tests for test module 209 — covers src modules [833, 834, 835, 836]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_833 import add_833
from module_834 import subtract_834
from module_835 import multiply_835
from module_836 import divide_836

def test_add_833():
    assert add_833(2, 3) == 5

def test_subtract_834():
    assert subtract_834(10, 4) == 6

def test_multiply_835():
    assert multiply_835(3, 7) == 21

def test_divide_836():
    assert divide_836(10, 2) == 5.0
