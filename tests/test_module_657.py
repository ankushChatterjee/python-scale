"""Tests for test module 657 — covers src modules [2625, 2626, 2627, 2628]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2625 import add_2625
from module_2626 import subtract_2626
from module_2627 import multiply_2627
from module_2628 import divide_2628

def test_add_2625():
    assert add_2625(2, 3) == 5

def test_subtract_2626():
    assert subtract_2626(10, 4) == 6

def test_multiply_2627():
    assert multiply_2627(3, 7) == 21

def test_divide_2628():
    assert divide_2628(10, 2) == 5.0
