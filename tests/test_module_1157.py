"""Tests for test module 1157 — covers src modules [4625, 4626, 4627, 4628]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4625 import add_4625
from module_4626 import subtract_4626
from module_4627 import multiply_4627
from module_4628 import divide_4628

def test_add_4625():
    assert add_4625(2, 3) == 5

def test_subtract_4626():
    assert subtract_4626(10, 4) == 6

def test_multiply_4627():
    assert multiply_4627(3, 7) == 21

def test_divide_4628():
    assert divide_4628(10, 2) == 5.0
