"""Tests for module 32."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_32 import subtract_32, divide_32, min_32, modulo_32

def test_subtract_32():
    assert subtract_32(10, 4) == 6

def test_divide_32():
    assert divide_32(10, 2) == 5.0

def test_min_32():
    assert min_32(3, 7) == 3

def test_modulo_32():
    assert modulo_32(10, 3) == 1
