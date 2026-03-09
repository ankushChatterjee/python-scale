"""Tests for module 85."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_85 import modulo_85, subtract_85, multiply_85, add_85

def test_modulo_85():
    assert modulo_85(10, 3) == 1

def test_subtract_85():
    assert subtract_85(10, 4) == 6

def test_multiply_85():
    assert multiply_85(3, 7) == 21

def test_add_85():
    assert add_85(2, 3) == 5
