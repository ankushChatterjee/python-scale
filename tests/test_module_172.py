"""Tests for module 172."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_172 import modulo_172, min_172, multiply_172, subtract_172

def test_modulo_172():
    assert modulo_172(10, 3) == 1

def test_min_172():
    assert min_172(3, 7) == 3

def test_multiply_172():
    assert multiply_172(3, 7) == 21

def test_subtract_172():
    assert subtract_172(10, 4) == 6
