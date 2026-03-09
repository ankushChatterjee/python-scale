"""Tests for test module 2193 — covers src modules [8769, 8770, 8771, 8772]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8769 import add_8769
from module_8770 import subtract_8770
from module_8771 import multiply_8771
from module_8772 import divide_8772

def test_add_8769():
    assert add_8769(2, 3) == 5

def test_subtract_8770():
    assert subtract_8770(10, 4) == 6

def test_multiply_8771():
    assert multiply_8771(3, 7) == 21

def test_divide_8772():
    assert divide_8772(10, 2) == 5.0
