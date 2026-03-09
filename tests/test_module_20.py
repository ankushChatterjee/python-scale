"""Tests for module 20."""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))
from module_20 import multiply_20, modulo_20, power_20, subtract_20

def test_multiply_20():
    assert multiply_20(3, 7) == 21

def test_modulo_20():
    assert modulo_20(10, 3) == 1

def test_power_20():
    assert power_20(2, 8) == 256

def test_subtract_20():
    assert subtract_20(10, 4) == 6
