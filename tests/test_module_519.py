"""Tests for test module 519 — covers src modules [2073, 2074, 2075, 2076]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_2073 import add_2073
from module_2074 import subtract_2074
from module_2075 import multiply_2075
from module_2076 import divide_2076

def test_add_2073():
    assert add_2073(2, 3) == 5

def test_subtract_2074():
    assert subtract_2074(10, 4) == 6

def test_multiply_2075():
    assert multiply_2075(3, 7) == 21

def test_divide_2076():
    assert divide_2076(10, 2) == 5.0
