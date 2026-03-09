"""Tests for module 201."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_201 import modulo_201, multiply_201, subtract_201, add_201

def test_modulo_201():
    assert modulo_201(10, 3) == 1

def test_multiply_201():
    assert multiply_201(3, 7) == 21

def test_subtract_201():
    assert subtract_201(10, 4) == 6

def test_add_201():
    assert add_201(2, 3) == 5
