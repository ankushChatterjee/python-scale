"""Tests for test module 1443 — covers src modules [5769, 5770, 5771, 5772]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5769 import add_5769
from module_5770 import subtract_5770
from module_5771 import multiply_5771
from module_5772 import divide_5772

def test_add_5769():
    assert add_5769(2, 3) == 5

def test_subtract_5770():
    assert subtract_5770(10, 4) == 6

def test_multiply_5771():
    assert multiply_5771(3, 7) == 21

def test_divide_5772():
    assert divide_5772(10, 2) == 5.0
