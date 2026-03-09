"""Tests for module 226."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_226 import modulo_226, add_226, subtract_226, multiply_226

def test_modulo_226():
    assert modulo_226(10, 3) == 1

def test_add_226():
    assert add_226(2, 3) == 5

def test_subtract_226():
    assert subtract_226(10, 4) == 6

def test_multiply_226():
    assert multiply_226(3, 7) == 21
