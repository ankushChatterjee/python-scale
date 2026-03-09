"""Tests for test module 2173 — covers src modules [8689, 8690, 8691, 8692]."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_8689 import add_8689
from module_8690 import subtract_8690
from module_8691 import multiply_8691
from module_8692 import divide_8692

def test_add_8689():
    assert add_8689(2, 3) == 5

def test_subtract_8690():
    assert subtract_8690(10, 4) == 6

def test_multiply_8691():
    assert multiply_8691(3, 7) == 21

def test_divide_8692():
    assert divide_8692(10, 2) == 5.0
