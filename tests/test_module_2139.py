"""Tests for test module 2139 — covers src modules [8553, 8554, 8555, 8556]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8553 import add_8553
from module_8554 import subtract_8554
from module_8555 import multiply_8555
from module_8556 import divide_8556

def test_add_8553():
    assert add_8553(2, 3) == 5

def test_subtract_8554():
    assert subtract_8554(10, 4) == 6

def test_multiply_8555():
    assert multiply_8555(3, 7) == 21

def test_divide_8556():
    assert divide_8556(10, 2) == 5.0
