"""Tests for test module 571 — covers src modules [2281, 2282, 2283, 2284]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2281 import add_2281
from module_2282 import subtract_2282
from module_2283 import multiply_2283
from module_2284 import divide_2284

def test_add_2281():
    assert add_2281(2, 3) == 5

def test_subtract_2282():
    assert subtract_2282(10, 4) == 6

def test_multiply_2283():
    assert multiply_2283(3, 7) == 21

def test_divide_2284():
    assert divide_2284(10, 2) == 5.0
