"""Tests for module 130."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_130 import divide_130, modulo_130, max_130, subtract_130

def test_divide_130():
    assert divide_130(10, 2) == 5.0

def test_modulo_130():
    assert modulo_130(10, 3) == 1

def test_max_130():
    assert max_130(3, 7) == 7

def test_subtract_130():
    assert subtract_130(10, 4) == 6
