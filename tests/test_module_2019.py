"""Tests for test module 2019 — covers src modules [8073, 8074, 8075, 8076]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8073 import add_8073
from module_8074 import subtract_8074
from module_8075 import multiply_8075
from module_8076 import divide_8076

def test_add_8073():
    assert add_8073(2, 3) == 5

def test_subtract_8074():
    assert subtract_8074(10, 4) == 6

def test_multiply_8075():
    assert multiply_8075(3, 7) == 21

def test_divide_8076():
    assert divide_8076(10, 2) == 5.0
