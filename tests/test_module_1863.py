"""Tests for test module 1863 — covers src modules [7449, 7450, 7451, 7452]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7449 import add_7449
from module_7450 import subtract_7450
from module_7451 import multiply_7451
from module_7452 import divide_7452

def test_add_7449():
    assert add_7449(2, 3) == 5

def test_subtract_7450():
    assert subtract_7450(10, 4) == 6

def test_multiply_7451():
    assert multiply_7451(3, 7) == 21

def test_divide_7452():
    assert divide_7452(10, 2) == 5.0
