"""Tests for module 249."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_249 import min_249, add_249, subtract_249, modulo_249

def test_min_249():
    assert min_249(3, 7) == 3

def test_add_249():
    assert add_249(2, 3) == 5

def test_subtract_249():
    assert subtract_249(10, 4) == 6

def test_modulo_249():
    assert modulo_249(10, 3) == 1
