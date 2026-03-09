"""Tests for module 7."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_7 import modulo_7, min_7, add_7, subtract_7

def test_modulo_7():
    assert modulo_7(10, 3) == 1

def test_min_7():
    assert min_7(3, 7) == 3

def test_add_7():
    assert add_7(2, 3) == 5

def test_subtract_7():
    assert subtract_7(10, 4) == 6
