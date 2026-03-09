"""Tests for test module 2295 — covers src modules [9177, 9178, 9179, 9180]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9177 import add_9177
from module_9178 import subtract_9178
from module_9179 import multiply_9179
from module_9180 import divide_9180

def test_add_9177():
    assert add_9177(2, 3) == 5

def test_subtract_9178():
    assert subtract_9178(10, 4) == 6

def test_multiply_9179():
    assert multiply_9179(3, 7) == 21

def test_divide_9180():
    assert divide_9180(10, 2) == 5.0
