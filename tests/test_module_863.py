"""Tests for test module 863 — covers src modules [3449, 3450, 3451, 3452]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3449 import add_3449
from module_3450 import subtract_3450
from module_3451 import multiply_3451
from module_3452 import divide_3452

def test_add_3449():
    assert add_3449(2, 3) == 5

def test_subtract_3450():
    assert subtract_3450(10, 4) == 6

def test_multiply_3451():
    assert multiply_3451(3, 7) == 21

def test_divide_3452():
    assert divide_3452(10, 2) == 5.0
