"""Tests for test module 1095 — covers src modules [4377, 4378, 4379, 4380]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4377 import add_4377
from module_4378 import subtract_4378
from module_4379 import multiply_4379
from module_4380 import divide_4380

def test_add_4377():
    assert add_4377(2, 3) == 5

def test_subtract_4378():
    assert subtract_4378(10, 4) == 6

def test_multiply_4379():
    assert multiply_4379(3, 7) == 21

def test_divide_4380():
    assert divide_4380(10, 2) == 5.0
