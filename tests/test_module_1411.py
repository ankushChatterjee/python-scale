"""Tests for test module 1411 — covers src modules [5641, 5642, 5643, 5644]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5641 import add_5641
from module_5642 import subtract_5642
from module_5643 import multiply_5643
from module_5644 import divide_5644

def test_add_5641():
    assert add_5641(2, 3) == 5

def test_subtract_5642():
    assert subtract_5642(10, 4) == 6

def test_multiply_5643():
    assert multiply_5643(3, 7) == 21

def test_divide_5644():
    assert divide_5644(10, 2) == 5.0
