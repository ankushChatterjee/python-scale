"""Tests for test module 903 — covers src modules [3609, 3610, 3611, 3612]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3609 import add_3609
from module_3610 import subtract_3610
from module_3611 import multiply_3611
from module_3612 import divide_3612

def test_add_3609():
    assert add_3609(2, 3) == 5

def test_subtract_3610():
    assert subtract_3610(10, 4) == 6

def test_multiply_3611():
    assert multiply_3611(3, 7) == 21

def test_divide_3612():
    assert divide_3612(10, 2) == 5.0
