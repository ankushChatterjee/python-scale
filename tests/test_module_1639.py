"""Tests for test module 1639 — covers src modules [6553, 6554, 6555, 6556]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6553 import add_6553
from module_6554 import subtract_6554
from module_6555 import multiply_6555
from module_6556 import divide_6556

def test_add_6553():
    assert add_6553(2, 3) == 5

def test_subtract_6554():
    assert subtract_6554(10, 4) == 6

def test_multiply_6555():
    assert multiply_6555(3, 7) == 21

def test_divide_6556():
    assert divide_6556(10, 2) == 5.0
