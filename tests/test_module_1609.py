"""Tests for test module 1609 — covers src modules [6433, 6434, 6435, 6436]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6433 import add_6433
from module_6434 import subtract_6434
from module_6435 import multiply_6435
from module_6436 import divide_6436

def test_add_6433():
    assert add_6433(2, 3) == 5

def test_subtract_6434():
    assert subtract_6434(10, 4) == 6

def test_multiply_6435():
    assert multiply_6435(3, 7) == 21

def test_divide_6436():
    assert divide_6436(10, 2) == 5.0
