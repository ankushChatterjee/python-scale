"""Tests for test module 2109 — covers src modules [8433, 8434, 8435, 8436]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8433 import add_8433
from module_8434 import subtract_8434
from module_8435 import multiply_8435
from module_8436 import divide_8436

def test_add_8433():
    assert add_8433(2, 3) == 5

def test_subtract_8434():
    assert subtract_8434(10, 4) == 6

def test_multiply_8435():
    assert multiply_8435(3, 7) == 21

def test_divide_8436():
    assert divide_8436(10, 2) == 5.0
