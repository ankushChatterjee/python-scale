"""Tests for module 33."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_33 import max_33, modulo_33, multiply_33, min_33

def test_max_33():
    assert max_33(3, 7) == 7

def test_modulo_33():
    assert modulo_33(10, 3) == 1

def test_multiply_33():
    assert multiply_33(3, 7) == 21

def test_min_33():
    assert min_33(3, 7) == 3
