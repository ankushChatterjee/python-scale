"""Tests for test module 1911 — covers src modules [7641, 7642, 7643, 7644]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7641 import add_7641
from module_7642 import subtract_7642
from module_7643 import multiply_7643
from module_7644 import divide_7644

def test_add_7641():
    assert add_7641(2, 3) == 5

def test_subtract_7642():
    assert subtract_7642(10, 4) == 6

def test_multiply_7643():
    assert multiply_7643(3, 7) == 21

def test_divide_7644():
    assert divide_7644(10, 2) == 5.0
