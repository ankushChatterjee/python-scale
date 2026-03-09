"""Tests for test module 661 — covers src modules [2641, 2642, 2643, 2644]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2641 import add_2641
from module_2642 import subtract_2642
from module_2643 import multiply_2643
from module_2644 import divide_2644

def test_add_2641():
    assert add_2641(2, 3) == 5

def test_subtract_2642():
    assert subtract_2642(10, 4) == 6

def test_multiply_2643():
    assert multiply_2643(3, 7) == 21

def test_divide_2644():
    assert divide_2644(10, 2) == 5.0
