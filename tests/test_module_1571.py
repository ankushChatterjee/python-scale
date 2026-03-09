"""Tests for test module 1571 — covers src modules [6281, 6282, 6283, 6284]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6281 import add_6281
from module_6282 import subtract_6282
from module_6283 import multiply_6283
from module_6284 import divide_6284

def test_add_6281():
    assert add_6281(2, 3) == 5

def test_subtract_6282():
    assert subtract_6282(10, 4) == 6

def test_multiply_6283():
    assert multiply_6283(3, 7) == 21

def test_divide_6284():
    assert divide_6284(10, 2) == 5.0
