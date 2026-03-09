"""Tests for module 186."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_186 import modulo_186, multiply_186, subtract_186, add_186

def test_modulo_186():
    assert modulo_186(10, 3) == 1

def test_multiply_186():
    assert multiply_186(3, 7) == 21

def test_subtract_186():
    assert subtract_186(10, 4) == 6

def test_add_186():
    assert add_186(2, 3) == 5
