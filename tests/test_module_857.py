"""Tests for test module 857 — covers src modules [3425, 3426, 3427, 3428]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3425 import add_3425
from module_3426 import subtract_3426
from module_3427 import multiply_3427
from module_3428 import divide_3428

def test_add_3425():
    assert add_3425(2, 3) == 5

def test_subtract_3426():
    assert subtract_3426(10, 4) == 6

def test_multiply_3427():
    assert multiply_3427(3, 7) == 21

def test_divide_3428():
    assert divide_3428(10, 2) == 5.0
