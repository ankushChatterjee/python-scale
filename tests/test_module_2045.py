"""Tests for test module 2045 — covers src modules [8177, 8178, 8179, 8180]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8177 import add_8177
from module_8178 import subtract_8178
from module_8179 import multiply_8179
from module_8180 import divide_8180

def test_add_8177():
    assert add_8177(2, 3) == 5

def test_subtract_8178():
    assert subtract_8178(10, 4) == 6

def test_multiply_8179():
    assert multiply_8179(3, 7) == 21

def test_divide_8180():
    assert divide_8180(10, 2) == 5.0
