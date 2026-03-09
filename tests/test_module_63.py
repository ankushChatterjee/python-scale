"""Tests for module 63."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_63 import modulo_63, divide_63, subtract_63, add_63

def test_modulo_63():
    assert modulo_63(10, 3) == 1

def test_divide_63():
    assert divide_63(10, 2) == 5.0

def test_subtract_63():
    assert subtract_63(10, 4) == 6

def test_add_63():
    assert add_63(2, 3) == 5
