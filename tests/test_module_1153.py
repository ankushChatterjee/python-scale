"""Tests for test module 1153 — covers src modules [4609, 4610, 4611, 4612]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4609 import add_4609
from module_4610 import subtract_4610
from module_4611 import multiply_4611
from module_4612 import divide_4612

def test_add_4609():
    assert add_4609(2, 3) == 5

def test_subtract_4610():
    assert subtract_4610(10, 4) == 6

def test_multiply_4611():
    assert multiply_4611(3, 7) == 21

def test_divide_4612():
    assert divide_4612(10, 2) == 5.0
