"""Tests for test module 1345 — covers src modules [5377, 5378, 5379, 5380]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5377 import add_5377
from module_5378 import subtract_5378
from module_5379 import multiply_5379
from module_5380 import divide_5380

def test_add_5377():
    assert add_5377(2, 3) == 5

def test_subtract_5378():
    assert subtract_5378(10, 4) == 6

def test_multiply_5379():
    assert multiply_5379(3, 7) == 21

def test_divide_5380():
    assert divide_5380(10, 2) == 5.0
