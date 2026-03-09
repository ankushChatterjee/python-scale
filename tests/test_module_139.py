"""Tests for module 139."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_139 import divide_139, subtract_139, power_139, modulo_139

def test_divide_139():
    assert divide_139(10, 2) == 5.0

def test_subtract_139():
    assert subtract_139(10, 4) == 6

def test_power_139():
    assert power_139(2, 8) == 256

def test_modulo_139():
    assert modulo_139(10, 3) == 1
