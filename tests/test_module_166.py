"""Tests for module 166."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_166 import subtract_166, divide_166, add_166, modulo_166

def test_subtract_166():
    assert subtract_166(10, 4) == 6

def test_divide_166():
    assert divide_166(10, 2) == 5.0

def test_add_166():
    assert add_166(2, 3) == 5

def test_modulo_166():
    assert modulo_166(10, 3) == 1
