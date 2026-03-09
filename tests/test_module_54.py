"""Tests for module 54."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_54 import subtract_54, modulo_54, max_54, multiply_54

def test_subtract_54():
    assert subtract_54(10, 4) == 6

def test_modulo_54():
    assert modulo_54(10, 3) == 1

def test_max_54():
    assert max_54(3, 7) == 7

def test_multiply_54():
    assert multiply_54(3, 7) == 21
