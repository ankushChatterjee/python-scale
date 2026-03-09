"""Tests for test module 1107 — covers src modules [4425, 4426, 4427, 4428]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4425 import add_4425
from module_4426 import subtract_4426
from module_4427 import multiply_4427
from module_4428 import divide_4428

def test_add_4425():
    assert add_4425(2, 3) == 5

def test_subtract_4426():
    assert subtract_4426(10, 4) == 6

def test_multiply_4427():
    assert multiply_4427(3, 7) == 21

def test_divide_4428():
    assert divide_4428(10, 2) == 5.0
