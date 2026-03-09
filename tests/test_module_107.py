"""Tests for test module 107 — covers src modules [425, 426, 427, 428]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_425 import add_425
from module_426 import subtract_426
from module_427 import multiply_427
from module_428 import divide_428

def test_add_425():
    assert add_425(2, 3) == 5

def test_subtract_426():
    assert subtract_426(10, 4) == 6

def test_multiply_427():
    assert multiply_427(3, 7) == 21

def test_divide_428():
    assert divide_428(10, 2) == 5.0
