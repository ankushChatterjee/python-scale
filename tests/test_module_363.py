"""Tests for test module 363 — covers src modules [1449, 1450, 1451, 1452]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1449 import add_1449
from module_1450 import subtract_1450
from module_1451 import multiply_1451
from module_1452 import divide_1452

def test_add_1449():
    assert add_1449(2, 3) == 5

def test_subtract_1450():
    assert subtract_1450(10, 4) == 6

def test_multiply_1451():
    assert multiply_1451(3, 7) == 21

def test_divide_1452():
    assert divide_1452(10, 2) == 5.0
