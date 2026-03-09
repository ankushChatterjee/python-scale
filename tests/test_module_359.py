"""Tests for test module 359 — covers src modules [1433, 1434, 1435, 1436]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1433 import add_1433
from module_1434 import subtract_1434
from module_1435 import multiply_1435
from module_1436 import divide_1436

def test_add_1433():
    assert add_1433(2, 3) == 5

def test_subtract_1434():
    assert subtract_1434(10, 4) == 6

def test_multiply_1435():
    assert multiply_1435(3, 7) == 21

def test_divide_1436():
    assert divide_1436(10, 2) == 5.0
