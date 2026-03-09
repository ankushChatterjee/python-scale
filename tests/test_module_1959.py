"""Tests for test module 1959 — covers src modules [7833, 7834, 7835, 7836]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7833 import add_7833
from module_7834 import subtract_7834
from module_7835 import multiply_7835
from module_7836 import divide_7836

def test_add_7833():
    assert add_7833(2, 3) == 5

def test_subtract_7834():
    assert subtract_7834(10, 4) == 6

def test_multiply_7835():
    assert multiply_7835(3, 7) == 21

def test_divide_7836():
    assert divide_7836(10, 2) == 5.0
