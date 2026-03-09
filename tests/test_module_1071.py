"""Tests for test module 1071 — covers src modules [4281, 4282, 4283, 4284]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4281 import add_4281
from module_4282 import subtract_4282
from module_4283 import multiply_4283
from module_4284 import divide_4284

def test_add_4281():
    assert add_4281(2, 3) == 5

def test_subtract_4282():
    assert subtract_4282(10, 4) == 6

def test_multiply_4283():
    assert multiply_4283(3, 7) == 21

def test_divide_4284():
    assert divide_4284(10, 2) == 5.0
