"""Tests for module 128."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_128 import modulo_128, subtract_128, divide_128, max_128

def test_modulo_128():
    assert modulo_128(10, 3) == 1

def test_subtract_128():
    assert subtract_128(10, 4) == 6

def test_divide_128():
    assert divide_128(10, 2) == 5.0

def test_max_128():
    assert max_128(3, 7) == 7
