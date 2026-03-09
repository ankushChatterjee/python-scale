"""Tests for test module 1407 — covers src modules [5625, 5626, 5627, 5628]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5625 import add_5625
from module_5626 import subtract_5626
from module_5627 import multiply_5627
from module_5628 import divide_5628

def test_add_5625():
    assert add_5625(2, 3) == 5

def test_subtract_5626():
    assert subtract_5626(10, 4) == 6

def test_multiply_5627():
    assert multiply_5627(3, 7) == 21

def test_divide_5628():
    assert divide_5628(10, 2) == 5.0
