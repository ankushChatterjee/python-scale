"""Tests for test module 1269 — covers src modules [5073, 5074, 5075, 5076]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5073 import add_5073
from module_5074 import subtract_5074
from module_5075 import multiply_5075
from module_5076 import divide_5076

def test_add_5073():
    assert add_5073(2, 3) == 5

def test_subtract_5074():
    assert subtract_5074(10, 4) == 6

def test_multiply_5075():
    assert multiply_5075(3, 7) == 21

def test_divide_5076():
    assert divide_5076(10, 2) == 5.0
