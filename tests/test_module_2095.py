"""Tests for test module 2095 — covers src modules [8377, 8378, 8379, 8380]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8377 import add_8377
from module_8378 import subtract_8378
from module_8379 import multiply_8379
from module_8380 import divide_8380

def test_add_8377():
    assert add_8377(2, 3) == 5

def test_subtract_8378():
    assert subtract_8378(10, 4) == 6

def test_multiply_8379():
    assert multiply_8379(3, 7) == 21

def test_divide_8380():
    assert divide_8380(10, 2) == 5.0
