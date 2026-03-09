"""Tests for test module 911 — covers src modules [3641, 3642, 3643, 3644]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3641 import add_3641
from module_3642 import subtract_3642
from module_3643 import multiply_3643
from module_3644 import divide_3644

def test_add_3641():
    assert add_3641(2, 3) == 5

def test_subtract_3642():
    assert subtract_3642(10, 4) == 6

def test_multiply_3643():
    assert multiply_3643(3, 7) == 21

def test_divide_3644():
    assert divide_3644(10, 2) == 5.0
