"""Tests for test module 595 — covers src modules [2377, 2378, 2379, 2380]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2377 import add_2377
from module_2378 import subtract_2378
from module_2379 import multiply_2379
from module_2380 import divide_2380

def test_add_2377():
    assert add_2377(2, 3) == 5

def test_subtract_2378():
    assert subtract_2378(10, 4) == 6

def test_multiply_2379():
    assert multiply_2379(3, 7) == 21

def test_divide_2380():
    assert divide_2380(10, 2) == 5.0
