"""Tests for test module 1019 — covers src modules [4073, 4074, 4075, 4076]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_4073 import add_4073
from module_4074 import subtract_4074
from module_4075 import multiply_4075
from module_4076 import divide_4076

def test_add_4073():
    assert add_4073(2, 3) == 5

def test_subtract_4074():
    assert subtract_4074(10, 4) == 6

def test_multiply_4075():
    assert multiply_4075(3, 7) == 21

def test_divide_4076():
    assert divide_4076(10, 2) == 5.0
