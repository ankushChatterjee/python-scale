"""Tests for module 145."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_145 import modulo_145, min_145, subtract_145, multiply_145

def test_modulo_145():
    assert modulo_145(10, 3) == 1

def test_min_145():
    assert min_145(3, 7) == 3

def test_subtract_145():
    assert subtract_145(10, 4) == 6

def test_multiply_145():
    assert multiply_145(3, 7) == 21
