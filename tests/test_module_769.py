"""Tests for test module 769 — covers src modules [3073, 3074, 3075, 3076]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_3073 import add_3073
from module_3074 import subtract_3074
from module_3075 import multiply_3075
from module_3076 import divide_3076

def test_add_3073():
    assert add_3073(2, 3) == 5

def test_subtract_3074():
    assert subtract_3074(10, 4) == 6

def test_multiply_3075():
    assert multiply_3075(3, 7) == 21

def test_divide_3076():
    assert divide_3076(10, 2) == 5.0
