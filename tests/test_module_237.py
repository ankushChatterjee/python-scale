"""Tests for module 237."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_237 import modulo_237, add_237, min_237, subtract_237

def test_modulo_237():
    assert modulo_237(10, 3) == 1

def test_add_237():
    assert add_237(2, 3) == 5

def test_min_237():
    assert min_237(3, 7) == 3

def test_subtract_237():
    assert subtract_237(10, 4) == 6
