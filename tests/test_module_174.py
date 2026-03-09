"""Tests for module 174."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_174 import subtract_174, modulo_174, add_174, multiply_174

def test_subtract_174():
    assert subtract_174(10, 4) == 6

def test_modulo_174():
    assert modulo_174(10, 3) == 1

def test_add_174():
    assert add_174(2, 3) == 5

def test_multiply_174():
    assert multiply_174(3, 7) == 21
