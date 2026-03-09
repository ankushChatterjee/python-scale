"""Tests for test module 907 — covers src modules [3625, 3626, 3627, 3628]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3625 import add_3625
from module_3626 import subtract_3626
from module_3627 import multiply_3627
from module_3628 import divide_3628

def test_add_3625():
    assert add_3625(2, 3) == 5

def test_subtract_3626():
    assert subtract_3626(10, 4) == 6

def test_multiply_3627():
    assert multiply_3627(3, 7) == 21

def test_divide_3628():
    assert divide_3628(10, 2) == 5.0
