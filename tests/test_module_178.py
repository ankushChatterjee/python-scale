"""Tests for module 178."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_178 import subtract_178, min_178, modulo_178, add_178

def test_subtract_178():
    assert subtract_178(10, 4) == 6

def test_min_178():
    assert min_178(3, 7) == 3

def test_modulo_178():
    assert modulo_178(10, 3) == 1

def test_add_178():
    assert add_178(2, 3) == 5
