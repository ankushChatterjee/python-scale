"""Tests for test module 2389 — covers src modules [9553, 9554, 9555, 9556]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_9553 import add_9553
from module_9554 import subtract_9554
from module_9555 import multiply_9555
from module_9556 import divide_9556

def test_add_9553():
    assert add_9553(2, 3) == 5

def test_subtract_9554():
    assert subtract_9554(10, 4) == 6

def test_multiply_9555():
    assert multiply_9555(3, 7) == 21

def test_divide_9556():
    assert divide_9556(10, 2) == 5.0
