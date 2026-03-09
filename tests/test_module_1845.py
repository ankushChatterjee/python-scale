"""Tests for test module 1845 — covers src modules [7377, 7378, 7379, 7380]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7377 import add_7377
from module_7378 import subtract_7378
from module_7379 import multiply_7379
from module_7380 import divide_7380

def test_add_7377():
    assert add_7377(2, 3) == 5

def test_subtract_7378():
    assert subtract_7378(10, 4) == 6

def test_multiply_7379():
    assert multiply_7379(3, 7) == 21

def test_divide_7380():
    assert divide_7380(10, 2) == 5.0
