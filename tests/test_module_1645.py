"""Tests for test module 1645 — covers src modules [6577, 6578, 6579, 6580]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6577 import add_6577
from module_6578 import subtract_6578
from module_6579 import multiply_6579
from module_6580 import divide_6580

def test_add_6577():
    assert add_6577(2, 3) == 5

def test_subtract_6578():
    assert subtract_6578(10, 4) == 6

def test_multiply_6579():
    assert multiply_6579(3, 7) == 21

def test_divide_6580():
    assert divide_6580(10, 2) == 5.0
