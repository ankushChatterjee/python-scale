"""Tests for module 171."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_171 import subtract_171, modulo_171, max_171, divide_171

def test_subtract_171():
    assert subtract_171(10, 4) == 6

def test_modulo_171():
    assert modulo_171(10, 3) == 1

def test_max_171():
    assert max_171(3, 7) == 7

def test_divide_171():
    assert divide_171(10, 2) == 5.0
