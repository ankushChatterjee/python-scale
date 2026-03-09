"""Tests for module 118."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_118 import subtract_118, divide_118, modulo_118, max_118

def test_subtract_118():
    assert subtract_118(10, 4) == 6

def test_divide_118():
    assert divide_118(10, 2) == 5.0

def test_modulo_118():
    assert modulo_118(10, 3) == 1

def test_max_118():
    assert max_118(3, 7) == 7
