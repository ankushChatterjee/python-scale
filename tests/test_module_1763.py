"""Tests for test module 1763 — covers src modules [7049, 7050, 7051, 7052]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7049 import add_7049
from module_7050 import subtract_7050
from module_7051 import multiply_7051
from module_7052 import divide_7052

def test_add_7049():
    assert add_7049(2, 3) == 5

def test_subtract_7050():
    assert subtract_7050(10, 4) == 6

def test_multiply_7051():
    assert multiply_7051(3, 7) == 21

def test_divide_7052():
    assert divide_7052(10, 2) == 5.0
