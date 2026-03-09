"""Tests for test module 1447 — covers src modules [5785, 5786, 5787, 5788]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5785 import add_5785
from module_5786 import subtract_5786
from module_5787 import multiply_5787
from module_5788 import divide_5788

def test_add_5785():
    assert add_5785(2, 3) == 5

def test_subtract_5786():
    assert subtract_5786(10, 4) == 6

def test_multiply_5787():
    assert multiply_5787(3, 7) == 21

def test_divide_5788():
    assert divide_5788(10, 2) == 5.0
