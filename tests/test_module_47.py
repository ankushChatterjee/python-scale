"""Tests for module 47."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_47 import min_47, subtract_47, modulo_47, max_47

def test_min_47():
    assert min_47(3, 7) == 3

def test_subtract_47():
    assert subtract_47(10, 4) == 6

def test_modulo_47():
    assert modulo_47(10, 3) == 1

def test_max_47():
    assert max_47(3, 7) == 7
