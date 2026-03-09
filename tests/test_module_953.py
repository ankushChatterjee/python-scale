"""Tests for test module 953 — covers src modules [3809, 3810, 3811, 3812]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3809 import add_3809
from module_3810 import subtract_3810
from module_3811 import multiply_3811
from module_3812 import divide_3812

def test_add_3809():
    assert add_3809(2, 3) == 5

def test_subtract_3810():
    assert subtract_3810(10, 4) == 6

def test_multiply_3811():
    assert multiply_3811(3, 7) == 21

def test_divide_3812():
    assert divide_3812(10, 2) == 5.0
