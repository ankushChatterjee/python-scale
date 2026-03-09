"""Tests for test module 1295 — covers src modules [5177, 5178, 5179, 5180]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5177 import add_5177
from module_5178 import subtract_5178
from module_5179 import multiply_5179
from module_5180 import divide_5180

def test_add_5177():
    assert add_5177(2, 3) == 5

def test_subtract_5178():
    assert subtract_5178(10, 4) == 6

def test_multiply_5179():
    assert multiply_5179(3, 7) == 21

def test_divide_5180():
    assert divide_5180(10, 2) == 5.0
