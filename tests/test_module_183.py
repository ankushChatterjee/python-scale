"""Tests for module 183."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_183 import multiply_183, divide_183, subtract_183, modulo_183

def test_multiply_183():
    assert multiply_183(3, 7) == 21

def test_divide_183():
    assert divide_183(10, 2) == 5.0

def test_subtract_183():
    assert subtract_183(10, 4) == 6

def test_modulo_183():
    assert modulo_183(10, 3) == 1
