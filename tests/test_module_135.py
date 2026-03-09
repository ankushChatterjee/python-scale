"""Tests for module 135."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_135 import subtract_135, divide_135, min_135, modulo_135

def test_subtract_135():
    assert subtract_135(10, 4) == 6

def test_divide_135():
    assert divide_135(10, 2) == 5.0

def test_min_135():
    assert min_135(3, 7) == 3

def test_modulo_135():
    assert modulo_135(10, 3) == 1
