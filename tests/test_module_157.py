"""Tests for test module 157 — covers src modules [625, 626, 627, 628]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_625 import add_625
from module_626 import subtract_626
from module_627 import multiply_627
from module_628 import divide_628

def test_add_625():
    assert add_625(2, 3) == 5

def test_subtract_626():
    assert subtract_626(10, 4) == 6

def test_multiply_627():
    assert multiply_627(3, 7) == 21

def test_divide_628():
    assert divide_628(10, 2) == 5.0
