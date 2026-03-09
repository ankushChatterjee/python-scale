"""Tests for module 210."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_210 import subtract_210, min_210, add_210, modulo_210

def test_subtract_210():
    assert subtract_210(10, 4) == 6

def test_min_210():
    assert min_210(3, 7) == 3

def test_add_210():
    assert add_210(2, 3) == 5

def test_modulo_210():
    assert modulo_210(10, 3) == 1
