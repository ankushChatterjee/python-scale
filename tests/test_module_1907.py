"""Tests for test module 1907 — covers src modules [7625, 7626, 7627, 7628]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7625 import add_7625
from module_7626 import subtract_7626
from module_7627 import multiply_7627
from module_7628 import divide_7628

def test_add_7625():
    assert add_7625(2, 3) == 5

def test_subtract_7626():
    assert subtract_7626(10, 4) == 6

def test_multiply_7627():
    assert multiply_7627(3, 7) == 21

def test_divide_7628():
    assert divide_7628(10, 2) == 5.0
