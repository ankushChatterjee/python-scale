"""Tests for test module 1795 — covers src modules [7177, 7178, 7179, 7180]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7177 import add_7177
from module_7178 import subtract_7178
from module_7179 import multiply_7179
from module_7180 import divide_7180

def test_add_7177():
    assert add_7177(2, 3) == 5

def test_subtract_7178():
    assert subtract_7178(10, 4) == 6

def test_multiply_7179():
    assert multiply_7179(3, 7) == 21

def test_divide_7180():
    assert divide_7180(10, 2) == 5.0
