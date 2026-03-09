"""Tests for test module 821 — covers src modules [3281, 3282, 3283, 3284]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3281 import add_3281
from module_3282 import subtract_3282
from module_3283 import multiply_3283
from module_3284 import divide_3284

def test_add_3281():
    assert add_3281(2, 3) == 5

def test_subtract_3282():
    assert subtract_3282(10, 4) == 6

def test_multiply_3283():
    assert multiply_3283(3, 7) == 21

def test_divide_3284():
    assert divide_3284(10, 2) == 5.0
