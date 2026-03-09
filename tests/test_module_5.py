"""Tests for module 5."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_5 import add_5, modulo_5, subtract_5, min_5

def test_add_5():
    assert add_5(2, 3) == 5

def test_modulo_5():
    assert modulo_5(10, 3) == 1

def test_subtract_5():
    assert subtract_5(10, 4) == 6

def test_min_5():
    assert min_5(3, 7) == 3
