"""Tests for test module 1045 — covers src modules [4177, 4178, 4179, 4180]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4177 import add_4177
from module_4178 import subtract_4178
from module_4179 import multiply_4179
from module_4180 import divide_4180

def test_add_4177():
    assert add_4177(2, 3) == 5

def test_subtract_4178():
    assert subtract_4178(10, 4) == 6

def test_multiply_4179():
    assert multiply_4179(3, 7) == 21

def test_divide_4180():
    assert divide_4180(10, 2) == 5.0
