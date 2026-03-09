"""Tests for test module 1595 — covers src modules [6377, 6378, 6379, 6380]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6377 import add_6377
from module_6378 import subtract_6378
from module_6379 import multiply_6379
from module_6380 import divide_6380

def test_add_6377():
    assert add_6377(2, 3) == 5

def test_subtract_6378():
    assert subtract_6378(10, 4) == 6

def test_multiply_6379():
    assert multiply_6379(3, 7) == 21

def test_divide_6380():
    assert divide_6380(10, 2) == 5.0
