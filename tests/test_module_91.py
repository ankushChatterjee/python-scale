"""Tests for module 91."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_91 import modulo_91, multiply_91, max_91, subtract_91

def test_modulo_91():
    assert modulo_91(10, 3) == 1

def test_multiply_91():
    assert multiply_91(3, 7) == 21

def test_max_91():
    assert max_91(3, 7) == 7

def test_subtract_91():
    assert subtract_91(10, 4) == 6
