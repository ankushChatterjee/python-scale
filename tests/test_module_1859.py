"""Tests for test module 1859 — covers src modules [7433, 7434, 7435, 7436]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7433 import add_7433
from module_7434 import subtract_7434
from module_7435 import multiply_7435
from module_7436 import divide_7436

def test_add_7433():
    assert add_7433(2, 3) == 5

def test_subtract_7434():
    assert subtract_7434(10, 4) == 6

def test_multiply_7435():
    assert multiply_7435(3, 7) == 21

def test_divide_7436():
    assert divide_7436(10, 2) == 5.0
