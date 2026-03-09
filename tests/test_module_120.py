"""Tests for module 120."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_120 import add_120, modulo_120, min_120, subtract_120

def test_add_120():
    assert add_120(2, 3) == 5

def test_modulo_120():
    assert modulo_120(10, 3) == 1

def test_min_120():
    assert min_120(3, 7) == 3

def test_subtract_120():
    assert subtract_120(10, 4) == 6
