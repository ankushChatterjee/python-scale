"""Tests for test module 795 — covers src modules [3177, 3178, 3179, 3180]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3177 import add_3177
from module_3178 import subtract_3178
from module_3179 import multiply_3179
from module_3180 import divide_3180

def test_add_3177():
    assert add_3177(2, 3) == 5

def test_subtract_3178():
    assert subtract_3178(10, 4) == 6

def test_multiply_3179():
    assert multiply_3179(3, 7) == 21

def test_divide_3180():
    assert divide_3180(10, 2) == 5.0
