"""Tests for module 216."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_216 import subtract_216, max_216, add_216, modulo_216

def test_subtract_216():
    assert subtract_216(10, 4) == 6

def test_max_216():
    assert max_216(3, 7) == 7

def test_add_216():
    assert add_216(2, 3) == 5

def test_modulo_216():
    assert modulo_216(10, 3) == 1
