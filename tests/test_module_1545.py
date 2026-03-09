"""Tests for test module 1545 — covers src modules [6177, 6178, 6179, 6180]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6177 import add_6177
from module_6178 import subtract_6178
from module_6179 import multiply_6179
from module_6180 import divide_6180

def test_add_6177():
    assert add_6177(2, 3) == 5

def test_subtract_6178():
    assert subtract_6178(10, 4) == 6

def test_multiply_6179():
    assert multiply_6179(3, 7) == 21

def test_divide_6180():
    assert divide_6180(10, 2) == 5.0
