"""Tests for test module 1769 — covers src modules [7073, 7074, 7075, 7076]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7073 import add_7073
from module_7074 import subtract_7074
from module_7075 import multiply_7075
from module_7076 import divide_7076

def test_add_7073():
    assert add_7073(2, 3) == 5

def test_subtract_7074():
    assert subtract_7074(10, 4) == 6

def test_multiply_7075():
    assert multiply_7075(3, 7) == 21

def test_divide_7076():
    assert divide_7076(10, 2) == 5.0
