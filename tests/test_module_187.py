"""Tests for module 187."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_187 import modulo_187, divide_187, subtract_187, min_187

def test_modulo_187():
    assert modulo_187(10, 3) == 1

def test_divide_187():
    assert divide_187(10, 2) == 5.0

def test_subtract_187():
    assert subtract_187(10, 4) == 6

def test_min_187():
    assert min_187(3, 7) == 3
