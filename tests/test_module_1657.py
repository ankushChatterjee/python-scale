"""Tests for test module 1657 — covers src modules [6625, 6626, 6627, 6628]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6625 import add_6625
from module_6626 import subtract_6626
from module_6627 import multiply_6627
from module_6628 import divide_6628

def test_add_6625():
    assert add_6625(2, 3) == 5

def test_subtract_6626():
    assert subtract_6626(10, 4) == 6

def test_multiply_6627():
    assert multiply_6627(3, 7) == 21

def test_divide_6628():
    assert divide_6628(10, 2) == 5.0
