"""Tests for test module 1821 — covers src modules [7281, 7282, 7283, 7284]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7281 import add_7281
from module_7282 import subtract_7282
from module_7283 import multiply_7283
from module_7284 import divide_7284

def test_add_7281():
    assert add_7281(2, 3) == 5

def test_subtract_7282():
    assert subtract_7282(10, 4) == 6

def test_multiply_7283():
    assert multiply_7283(3, 7) == 21

def test_divide_7284():
    assert divide_7284(10, 2) == 5.0
