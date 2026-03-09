"""Tests for module 196."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_196 import modulo_196, subtract_196, divide_196, min_196

def test_modulo_196():
    assert modulo_196(10, 3) == 1

def test_subtract_196():
    assert subtract_196(10, 4) == 6

def test_divide_196():
    assert divide_196(10, 2) == 5.0

def test_min_196():
    assert min_196(3, 7) == 3
