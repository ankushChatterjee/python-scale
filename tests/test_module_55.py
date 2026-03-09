"""Tests for module 55."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_55 import max_55, subtract_55, modulo_55, min_55

def test_max_55():
    assert max_55(3, 7) == 7

def test_subtract_55():
    assert subtract_55(10, 4) == 6

def test_modulo_55():
    assert modulo_55(10, 3) == 1

def test_min_55():
    assert min_55(3, 7) == 3
