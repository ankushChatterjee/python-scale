"""Tests for test module 1943 — covers src modules [7769, 7770, 7771, 7772]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7769 import add_7769
from module_7770 import subtract_7770
from module_7771 import multiply_7771
from module_7772 import divide_7772

def test_add_7769():
    assert add_7769(2, 3) == 5

def test_subtract_7770():
    assert subtract_7770(10, 4) == 6

def test_multiply_7771():
    assert multiply_7771(3, 7) == 21

def test_divide_7772():
    assert divide_7772(10, 2) == 5.0
