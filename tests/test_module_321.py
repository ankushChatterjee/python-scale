"""Tests for test module 321 — covers src modules [1281, 1282, 1283, 1284]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_1281 import add_1281
from module_1282 import subtract_1282
from module_1283 import multiply_1283
from module_1284 import divide_1284

def test_add_1281():
    assert add_1281(2, 3) == 5

def test_subtract_1282():
    assert subtract_1282(10, 4) == 6

def test_multiply_1283():
    assert multiply_1283(3, 7) == 21

def test_divide_1284():
    assert divide_1284(10, 2) == 5.0
