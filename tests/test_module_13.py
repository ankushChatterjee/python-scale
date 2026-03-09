"""Tests for test module 13 — covers src modules [49, 50, 51, 52]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_49 import add_49
from module_50 import subtract_50
from module_51 import multiply_51
from module_52 import divide_52

def test_add_49():
    assert add_49(2, 3) == 5

def test_subtract_50():
    assert subtract_50(10, 4) == 6

def test_multiply_51():
    assert multiply_51(3, 7) == 21

def test_divide_52():
    assert divide_52(10, 2) == 5.0
