"""Tests for module 205."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_205 import modulo_205, add_205, subtract_205, multiply_205

def test_modulo_205():
    assert modulo_205(10, 3) == 1

def test_add_205():
    assert add_205(2, 3) == 5

def test_subtract_205():
    assert subtract_205(10, 4) == 6

def test_multiply_205():
    assert multiply_205(3, 7) == 21
