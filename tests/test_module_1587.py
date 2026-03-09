"""Tests for test module 1587 — covers src modules [6345, 6346, 6347, 6348]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6345 import add_6345
from module_6346 import subtract_6346
from module_6347 import multiply_6347
from module_6348 import divide_6348

def test_add_6345():
    assert add_6345(2, 3) == 5

def test_subtract_6346():
    assert subtract_6346(10, 4) == 6

def test_multiply_6347():
    assert multiply_6347(3, 7) == 21

def test_divide_6348():
    assert divide_6348(10, 2) == 5.0
