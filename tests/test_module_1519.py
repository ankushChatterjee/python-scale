"""Tests for test module 1519 — covers src modules [6073, 6074, 6075, 6076]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_6073 import add_6073
from module_6074 import subtract_6074
from module_6075 import multiply_6075
from module_6076 import divide_6076

def test_add_6073():
    assert add_6073(2, 3) == 5

def test_subtract_6074():
    assert subtract_6074(10, 4) == 6

def test_multiply_6075():
    assert multiply_6075(3, 7) == 21

def test_divide_6076():
    assert divide_6076(10, 2) == 5.0
