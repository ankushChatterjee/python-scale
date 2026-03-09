"""Tests for module 140."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_140 import max_140, add_140, modulo_140, subtract_140

def test_max_140():
    assert max_140(3, 7) == 7

def test_add_140():
    assert add_140(2, 3) == 5

def test_modulo_140():
    assert modulo_140(10, 3) == 1

def test_subtract_140():
    assert subtract_140(10, 4) == 6
