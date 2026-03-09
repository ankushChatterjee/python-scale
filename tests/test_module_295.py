"""Tests for test module 295 — covers src modules [1177, 1178, 1179, 1180]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1177 import add_1177
from module_1178 import subtract_1178
from module_1179 import multiply_1179
from module_1180 import divide_1180

def test_add_1177():
    assert add_1177(2, 3) == 5

def test_subtract_1178():
    assert subtract_1178(10, 4) == 6

def test_multiply_1179():
    assert multiply_1179(3, 7) == 21

def test_divide_1180():
    assert divide_1180(10, 2) == 5.0
