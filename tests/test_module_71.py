"""Tests for test module 71 — covers src modules [281, 282, 283, 284]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_281 import add_281
from module_282 import subtract_282
from module_283 import multiply_283
from module_284 import divide_284

def test_add_281():
    assert add_281(2, 3) == 5

def test_subtract_282():
    assert subtract_282(10, 4) == 6

def test_multiply_283():
    assert multiply_283(3, 7) == 21

def test_divide_284():
    assert divide_284(10, 2) == 5.0
