"""Tests for test module 2071 — covers src modules [8281, 8282, 8283, 8284]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8281 import add_8281
from module_8282 import subtract_8282
from module_8283 import multiply_8283
from module_8284 import divide_8284

def test_add_8281():
    assert add_8281(2, 3) == 5

def test_subtract_8282():
    assert subtract_8282(10, 4) == 6

def test_multiply_8283():
    assert multiply_8283(3, 7) == 21

def test_divide_8284():
    assert divide_8284(10, 2) == 5.0
