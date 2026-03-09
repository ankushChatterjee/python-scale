"""Tests for module 13."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_13 import subtract_13, modulo_13, multiply_13, min_13

def test_subtract_13():
    assert subtract_13(10, 4) == 6

def test_modulo_13():
    assert modulo_13(10, 3) == 1

def test_multiply_13():
    assert multiply_13(3, 7) == 21

def test_min_13():
    assert min_13(3, 7) == 3
