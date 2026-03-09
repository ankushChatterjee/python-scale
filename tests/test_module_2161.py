"""Tests for test module 2161 — covers src modules [8641, 8642, 8643, 8644]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8641 import add_8641
from module_8642 import subtract_8642
from module_8643 import multiply_8643
from module_8644 import divide_8644

def test_add_8641():
    assert add_8641(2, 3) == 5

def test_subtract_8642():
    assert subtract_8642(10, 4) == 6

def test_multiply_8643():
    assert multiply_8643(3, 7) == 21

def test_divide_8644():
    assert divide_8644(10, 2) == 5.0
