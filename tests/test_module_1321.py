"""Tests for test module 1321 — covers src modules [5281, 5282, 5283, 5284]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5281 import add_5281
from module_5282 import subtract_5282
from module_5283 import multiply_5283
from module_5284 import divide_5284

def test_add_5281():
    assert add_5281(2, 3) == 5

def test_subtract_5282():
    assert subtract_5282(10, 4) == 6

def test_multiply_5283():
    assert multiply_5283(3, 7) == 21

def test_divide_5284():
    assert divide_5284(10, 2) == 5.0
