"""Tests for test module 113 — covers src modules [449, 450, 451, 452]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_449 import add_449
from module_450 import subtract_450
from module_451 import multiply_451
from module_452 import divide_452

def test_add_449():
    assert add_449(2, 3) == 5

def test_subtract_450():
    assert subtract_450(10, 4) == 6

def test_multiply_451():
    assert multiply_451(3, 7) == 21

def test_divide_452():
    assert divide_452(10, 2) == 5.0
